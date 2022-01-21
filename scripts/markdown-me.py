import sys
import markdown

source_file = sys.argv[1]
dest_file_name = sys.argv[2]
destination_file = "docs/" + str(dest_file_name)

print("Converting " + source_file)

with open(source_file, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open(destination_file, 'w') as f:
    f.write(html)

print(destination_file + " written!")