""" Script to generate HTML files from Markdown for publication """
import glob

import markdown

TEMPLATE_FILE = "template.html"

# Build out html files
for file_name in glob.iglob("**/**.md", recursive=True):

    print("Converting " + file_name + " to HTML")

    if file_name == "README.md":
        DESTINATION_FILE = "docs/index.html"
    else:
        DESTINATION_FILE = "docs/" + file_name.replace(".md", ".html")

    page_file = DESTINATION_FILE.split("/")[-1].replace(".html", "")
    index_file = DESTINATION_FILE.rsplit("/", 1)[0] + "/index.html"

    # Load Markdown content
    with open(file_name, "r", encoding="UTF-8") as f:
        text = f.read()
        html = markdown.markdown(
            text, extensions=["attr_list", "md_in_html", "markdown.extensions.tables"]
        )
        ## Fix paths from README
        html = html.replace("./docs/", "")

        # Append header block
        if "<!-- EndHead -->" in html:
            html = html.replace("<!-- EndHead -->", "</div></div>")
        else:
            html = "</div></div>" + html

    # Load header content
    with open(TEMPLATE_FILE, "r", encoding="UTF-8") as t:
        completed_template = t.read().replace("{{ BODY }}", html)

    # Build file
    with open(DESTINATION_FILE, "w", encoding="UTF-8") as a:
        a.write(completed_template)
    print(DESTINATION_FILE + " written!")

# Build out html files
for top_dir in glob.iglob("docs/pages/*"):
    # Write index file
    index_file = top_dir + "/index.html"
    page_title = top_dir.split("/")[2]
    print("Collecting pages for " + index_file)
    page_list = []

    for indexable_page in glob.iglob(top_dir + "/*"):
        if "index.html" not in indexable_page:
            link_name = indexable_page.split("/")[-1].replace(".html", "")
            page_list.append(link_name)

    # Build out index list
    html = "<ul>\n<h2>" + page_title + "</h2>"
    for page_file in sorted(page_list):
        page_title = page_file.replace("_", " ").capitalize()
        html = html + "<li><a href=" + page_file + ">" + page_title + "</a></li>\n"
    html = html + "</ul>\n"

    # Update template and save
    with open(TEMPLATE_FILE, "r", encoding="UTF-8") as t:
        completed_template = t.read().replace("{{ BODY }}", html)

    # Write index page
    with open(index_file, "w", encoding="UTF-8") as a:
        a.write(completed_template)
        print(index_file + " written!")
