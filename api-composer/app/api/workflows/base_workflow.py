
from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class WorkflowRequest:
    def __init__(self, description: str):
        self.description = description
        self.context = {"description": description}

    def update_context(self, key: str, value: Any):
        logger.info(f"Updating context: {key} = {value}")
        self.context[key] = value

    def get_context(self) -> Dict[str, Any]:
        return self.context

    def needs_more_info(self) -> bool:
        # Logic to determine if more information is needed
        return "missing_details" in self.context

    def get_final_output(self) -> Dict[str, Any]:
        return {"description": self.description, "context": self.context}

    def get(self, key: str, default=None):
        return self.context.get(key, default)


class BaseWorkflow(ABC):
    def __init__(self):
        self.handlers = []

    @abstractmethod
    async def execute(self, description: str) -> WorkflowRequest:
        pass

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)
