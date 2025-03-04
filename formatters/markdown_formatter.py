from .base_formatter import BaseFormatter
from models import Document, Flow, Step

class MarkdownFormatter(BaseFormatter):
    def format(self, document: Document) -> str:

        header_level_prefix = "#" #TODO make this configurable
        output = ""

        for flow in document.flows:
            list_item_no = 1

            output += "\n" + header_level_prefix + "# " + document.title + "\n\n"

            output += document.description + "\n\n"
            
            for i in flow.steps: # a step in a workflow
                output += header_level_prefix + "## " + str(list_item_no) + ": " + i.id + "\n\n"

                output += i.description + "\n\n"
                output += "- Operation: `" + i.operation_id + "`\n"

                if len(i.outputs) > 0:
                    out_list = ""
                    first = True
                    for o in i.outputs:
                        if first:
                            first = False
                        else:
                            out_list += ", "

                        out_list += o.name

                    output += "- Outputs: " + out_list + "\n"

                
                output += "\n"
                list_item_no = list_item_no + 1

        return output
