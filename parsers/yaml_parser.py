import yaml
from models.base import *

class YamlParser:
    @staticmethod
    def parse_file(file_path: str) -> Document:
        with open(file_path) as stream:
            try:
                data = yaml.safe_load(stream)
                
                doc = Document(
                    title=data.get('info', {}).get('title'),
                    description=data.get('info', {}).get('description', ''),
                    flows=[]
                )
                
                for f in data.get('workflows'):
                    workflow = Flow(
                            id=f['workflowId'],
                            steps=[]
                            )

                    for s in f['steps']:
                        step = (Step(
                            id=s['stepId'],
                            operation_id=s['operationId'],
                            description=s['description'],
                            ))

                        if 'outputs' in s.keys():
                            for o in s['outputs'].keys():
                                step.add_output(StepOutput(
                                    name=o
                                    ))

                        workflow.add_step(step)


                    doc.add_flow(workflow)

            except yaml.YAMLError as exc:
                print(exc)

        return doc
