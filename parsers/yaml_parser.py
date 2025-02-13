import yaml
from models import Document, Flow, Step

class YamlParser:
    @staticmethod
    def parse_file(file_path: str) -> Document:
        with open(file_path) as stream:
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

        return doc
