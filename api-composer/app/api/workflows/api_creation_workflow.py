from app.api.workflows.base_workflow import BaseWorkflow, WorkflowRequest
from app.api.handlers.langchain_handler import LangChainHandler
from app.services.openai_service import OpenAIService
import logging

logger = logging.getLogger(__name__)


class APICreationWorkflow(BaseWorkflow):
    def __init__(self):
        super().__init__()
        self.handlers = [
            LangChainHandler(OpenAIService().create_openai_chain()),
            # Additional handlers for refinement, saving, etc.
        ]

    async def execute(self, description: str) -> dict:
        logger.info(
            f"Starting workflow execution with description: {description}")
        request = WorkflowRequest(description=description)
        logger.info(
            f"Initial context after request creation: {request.get_context()}")
        try:
            for handler in self.handlers:
                request = handler.handle(request)
                logger.info(
                    f"Context after handler {handler}: {request.get_context()}")
                if request.needs_more_info():
                    logger.info(
                        f"Request needs more info: {request.get_context()}")
                    return self.ask_for_more_info(request)
                if "error" in request.get_context():
                    logger.error(
                        f"Error in workflow: {request.get_context().get('error')}")
                    break
            return request.get_final_output()
        except Exception as e:
            logger.exception(
                f"Exception occurred during workflow execution: {str(e)}")
            return {"status": "error", "message": str(e)}

    def ask_for_more_info(self, request):
        context = request.get_context()
        missing_details = context.get(
            "missing_details", "Please specify the missing parts.")
        return {"status": "incomplete", "missing_details": missing_details}
