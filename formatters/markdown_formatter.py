from .base_formatter import BaseFormatter
from models import Document, Flow, Step

class MarkdownFormatter(BaseFormatter):
    def format(self, document: Document) -> str:

        output = ""

        for flow in document.flows:
            list_item_no = 1

            output += "\n## " + document.title + "\n\n"
            
            for i in flow.steps: # a step in a workflow
                output += str(list_item_no) + ": " + i.id + "\n"
                
                list_item_no = list_item_no + 1

        return output
