import sys
import markdown
from pathlib import Path

source_file = Path(sys.argv[1])
destination_file = "docs/" + str(source_file.with_suffix('.html'))

with open(source_file, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open(destination_file, 'w') as f:
    f.write(html)