from operator import index
import sys
import markdown
import os
import glob

template_file = "template.html"

# Build out html files
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
    with open(template_file, 'r') as t:
        completed_template = t.read().replace("{{ BODY }}", html)

    # Build file
    with open(destination_file, 'w') as a:
        a.write(completed_template)
    print(destination_file + " written!")

# Build out html files
for top_dir in glob.iglob('docs/pages/*'):
    # Write index file
    index_file = top_dir + "/index.html"
    print("Collecting pages for " + index_file)
    page_list = []

    for indexable_page in glob.iglob(top_dir + "/*"):
        if "index.html" not in indexable_page:
            nice_name = indexable_page.split("/")[-1]
            page_list.append(nice_name)

    # Build out index list
    html = "<ul>"
    for page_file in page_list:
        html = html + "<a href=" + page_file + ">" + page_file + "</a>\n"
    html = html + "</ul>"

    # Update template and save
    with open(template_file, 'r') as t:
        completed_template = t.read().replace("{{ BODY }}", html)

    # Write index page
    with open(index_file, 'w') as a:
        a.write(completed_template)
        print(index_file + " written!")