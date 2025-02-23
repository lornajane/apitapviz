import argparse
from models import *
from parsers import YamlParser
from formatters import MermaidFormatter, MarkdownFormatter


def main():
    parser = argparse.ArgumentParser(description="Visual representation of OpenAPI Arazzo")
    parser.add_argument("arazzo_file", help="Arazzo file")

    parser.add_argument("--format", "-f", default="markdown",
                       help="Output format: markdown (default), mermaid")

    args = parser.parse_args()

    doc = YamlParser.parse_file(args.arazzo_file)
    # print(doc)

    if args.format == "mermaid":
        formatter = MermaidFormatter()
    else:
        formatter = MarkdownFormatter()

    # Now build chart
    m = formatter.format(doc)
    print(m)

if __name__ == "__main__":
    main()
