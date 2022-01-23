import sys
import markdown
import pdfkit

source_file = "README.md"
header_file = "header.html"
destination_file = "docs/index.html"

print("Converting " + source_file + " to HTML")

# Load Markdown content
with open(source_file, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)
    ## Fix paths from README
    html = html.replace('./docs/', "")

# Load header content
with open(header_file, 'r') as h:
    header = h.read()

with open(destination_file, 'w') as f:
    f.write(header)
    f.write(html)

print(destination_file + " written!")

# print("Storing PDF copy")
# pdfkit.from_file(destination_file, 'docs/static/tjth.pdf')