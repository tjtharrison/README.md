import sys
import markdown
import os
import glob

header_file = "header.html"
footer_file = "footer.html"
article_dir = "articles"

for file_name in glob.iglob('**/**.md', recursive=True):

    print("Converting " + file_name + " to HTML")

    if file_name == "README.md":
        destination_file = "docs/index.html"
    else:
        destination_file = ("docs/" + file_name.replace(".md",".html"))

    page_file = destination_file.split("/")[-1].replace(".html","")
    index_file = destination_file.rsplit("/", 1)[0] + "/index.html"

    # Load Markdown content
    with open(file_name, 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=['attr_list','md_in_html','markdown.extensions.tables'])
        ## Fix paths from README
        html = html.replace('./docs/', "")

        # Append header block
        if "<!-- EndHead -->" in html:
            html = html.replace("<!-- EndHead -->","</div></div>")
        else:
            html = "</div></div>" + html

    # Load header content
    with open(header_file, 'r') as h:
        header = h.read()

    # Load footer content
    with open(footer_file, 'r') as f:
        footer = f.read()

    # Build file
    with open(destination_file, 'w') as a:
        a.write(header)
        a.write(html)
        a.write(footer)

    if file_name != "README.md":
        # Update index
        print("Updating index: " + index_file)
        with open(index_file, 'a') as i:
            i.write("<a href=" + page_file + ">" + page_file + "</a>\n")

    print(destination_file + " written!")
