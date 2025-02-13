from models import *
from parsers import YamlParser
from formatters import MermaidFormatter, MarkdownFormatter
 
doc = YamlParser.parse_file("example2.yaml")

# print(doc)

# Now build chart
mermaid_formatter = MermaidFormatter()
m = mermaid_formatter.format(doc)
print(m)

markdown_formatter = MarkdownFormatter()
m = markdown_formatter.format(doc)
print(m)

