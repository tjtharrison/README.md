import sys
import markdown
import pdfkit

source_file = "README.md"
header_file = "header.html"
footer_file = "footer.html"
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

# Load footer content
with open(footer_file, 'r') as f:
    footer = f.read()


with open(destination_file, 'w') as a:
    a.write(header)
    a.write(html)
    a.write(footer)

print(destination_file + " written!")

# print("Storing PDF copy")
# pdfkit.from_file(destination_file, 'docs/static/tjth.pdf')