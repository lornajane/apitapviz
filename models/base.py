from dataclasses import dataclass, field
from typing import List

@dataclass
class StepOutput:
    name: str

@dataclass
class Step:
    id: str
    operation_id: str
    description: str
    outputs: List[StepOutput] = field(default_factory=list)

    def add_output(self, output: StepOutput):
        self.outputs.append(output)

@dataclass
class Flow:
    id: str
    steps: List[Step] = field(default_factory=list)

    def add_step(self, step: Step):
        self.steps.append(step)

@dataclass
class Document:
    title: str
    description: str
    flows: List[Flow] = field(default_factory=list)

    def add_flow(self, flow: Flow):
        self.flows.append(flow)
