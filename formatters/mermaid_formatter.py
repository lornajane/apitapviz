from .base_formatter import BaseFormatter
from models import Document, Flow, Step

from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Link
)

class MermaidFormatter(BaseFormatter):
    def format(self, document: Document) -> str:
        nodes = []
        links = []
        
        for flow in document.flows:
            prev_node = None
            
            for i in flow.steps: # a step in a workflow
                new_node = Node(i.id)
                nodes.append(new_node)
                
                # Add link if previous node exists
                if prev_node:
                    links.append(Link(prev_node, new_node))
                
                prev_node = new_node
        
        # Generate Mermaid diagram code
        m = MermaidDiagram(
            title=document.title,
            orientation="top-down",
            nodes=nodes,
            links=links
        )

        return m
