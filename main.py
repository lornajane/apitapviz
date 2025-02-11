from dataclasses import dataclass, field
from typing import List
import yaml
 
from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Interaction,
    Link
)

## Define data structures

@dataclass
class Step:
    id: str

@dataclass
class Flow:
    id: str
    steps: List[Step] = field(default_factory=list)

    def add_step(self, step: Step):
        self.steps.append(step)

@dataclass
class Document:
    title: str
    flows: List[Flow] = field(default_factory=list)

    def add_flow(self, flow: Flow):
        self.flows.append(flow)

# Parse source file (YAML only)

with open("example2.yaml") as stream:
    try:
        data = yaml.safe_load(stream)

        doc = Document(
                title=data.get('info')['title'],
                flows=[]
                )

        for f in data.get('workflows'):
            workflow = Flow(
                    id=f['workflowId'],
                    steps=[]
                    )

            for s in f['steps']:
                workflow.add_step(Step(
                    id=s['stepId']
                    ))

            doc.add_flow(workflow)

    except yaml.YAMLError as exc:
        print(exc)

# print(doc)

# Now build chart
nodes = []
links = []

for w in doc.flows:
    # reset per-workflow things

    prev = None
    for i in w.steps: # a step in a workflow
        new_node = Node(i.id)
        nodes.append(new_node)

        # link to the previous step by default
        if prev != None:
            links.append(Link(prev, new_node))

        prev = new_node # store the node name so we can link to it (it can be inflected)

m = MermaidDiagram(
    title=doc.title,
    orientation="top-down",
    nodes=nodes,
    links=links
)

print(m)

