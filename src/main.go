package main

import (
	"bytes"
	"os"

	"github.com/gomarkdown/markdown"
	"github.com/gomarkdown/markdown/html"
	"github.com/gomarkdown/markdown/parser"

	"github.com/rs/zerolog/log"
)

func convertMarkdown(fileName string) ([]byte, error) {

	fileContents, err := os.ReadFile(fileName)

	if err != nil {
		return []byte{}, err
	}

	// create markdown parser with extensions
	extensions := parser.CommonExtensions | parser.AutoHeadingIDs | parser.NoEmptyLineBeforeBlock | parser.Attributes
	p := parser.NewWithExtensions(extensions)
	doc := p.Parse(fileContents)

	// create HTML renderer with extensions
	htmlFlags := html.CommonFlags | html.HrefTargetBlank
	opts := html.RendererOptions{Flags: htmlFlags}
	renderer := html.NewRenderer(opts)

	return markdown.Render(doc, renderer), nil
}

func mergeTemplate(body []byte) ([]byte, error) {
	log.Info().Msg("Merging template with contents")

	templateContents, err := os.ReadFile("docs/template.html")

	if err != nil {
		return []byte{}, err
	}

	combinedHtml := bytes.Replace(templateContents, []byte("{{ BODY }}"), body, 1)

	return combinedHtml, nil
}

func processFile(fileName string) error {
	log.Info().Msg("Processing file: " + fileName)

	html, err := convertMarkdown(fileName)

	if err != nil {
		return err
	}

	// Combine template with body
	combinedHtml, err := mergeTemplate(html)

	if err != nil {
		return err
	}

	return os.WriteFile("../docs/index.html", combinedHtml, 0644)
}

func resolveStaticDir() error {
	log.Info().Msg("Processing static directory")
	staticDir := "../docs/static"

	_, err := os.Stat(staticDir)

	if err != nil {
		log.Info().Msg("Destination directory does not exist, copying")
		err := os.CopyFS(staticDir, os.DirFS("../static"))

		if err != nil {
			return err
		}
	} else {
		log.Info().Msg("Destination directory exists, deleting..")
		err := os.RemoveAll(staticDir)

		if err != nil {
			log.Error().Msg("Failed to delete directory: " + err.Error())
			return err
		} else {
			// Try once more to copy
			return resolveStaticDir()
		}
	}

	return nil
}

func main() {
	log.Info().Msg("Starting conversion of markdown to html")

	err := processFile("../README.md")

	if err != nil {
		panic("Failed to convert file! " + err.Error())
	}

	err = resolveStaticDir()

	if err != nil {
		panic("Failed to copy static directory!")
	}
}
