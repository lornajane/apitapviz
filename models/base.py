# workflow_processor/models/base.py
from dataclasses import dataclass, field
from typing import List

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
