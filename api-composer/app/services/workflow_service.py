from app.api.workflows.api_creation_workflow import APICreationWorkflow
from app.api.workflows.refinement_workflow import RefinementWorkflow


class WorkflowService:
    @staticmethod
    def get_workflow(workflow_name: str):
        if workflow_name == "api_creation":
            return APICreationWorkflow()
        elif workflow_name == "refinement":
            return RefinementWorkflow()
        # Add more workflows as needed
        raise ValueError(f"Unknown workflow: {workflow_name}")
