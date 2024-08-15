from langchain.chains import LLMChain
from app.api.workflows.base_workflow import WorkflowRequest
import logging

logger = logging.getLogger(__name__)


class LangChainHandler:
    def __init__(self, chain: LLMChain):
        self.chain = chain
        logger.info(
            f"LangChainHandler initialized with chain: {self.chain}"
        )

    def handle(self, request: WorkflowRequest) -> WorkflowRequest:
        context = request.get_context()
        logger.info(f"Context before running the chain: {context}")
        if 'description' not in context:
            raise ValueError(
                "The key 'description' is missing in the context."
            )
        response = self.chain.run(context)
        request.update_context(key="api_specification", value=response)
        logger.info(
            f"Context after running the chain: {request.get_context()}"
        )
        return request
