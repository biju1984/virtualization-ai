from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from app.api.handlers.langchain_handler import LangChainHandler
from app.api.workflows.base_workflow import WorkflowRequest


class RefinementWorkflow:
    def __init__(self):
        # Define the prompt template
        template = "You are a helpful assistant. Given the following description, refine the API specification: {description}"
        prompt = PromptTemplate(
            template=template, input_variables=["description"])

        # Create an LLMChain with OpenAI
        openai_model = OpenAI(temperature=0.5)
        chain = LLMChain(llm=openai_model, prompt=prompt)

        # Pass the LLMChain instance to the LangChainHandler
        self.langchain_handler = LangChainHandler(chain)

    async def execute(self, initial_response: dict, user_input: str) -> dict:
        """
        Execute the workflow to refine the API specification.
        """
        if not self.is_sufficient_info(initial_response):
            prompt = self.generate_refinement_prompt(initial_response)

            # Create a WorkflowRequest object
            request = WorkflowRequest(description=prompt)

            # If langchain_handler.handle() is async, then:
            # refined_response = await self.langchain_handler.handle(request)
            # If langchain_handler.handle() is sync, then:
            refined_response = self.langchain_handler.handle(request)

            return refined_response.get_final_output()
        else:
            return self.process_full_response(initial_response)

    def is_sufficient_info(self, response: dict) -> bool:
        """
        Determine if the response has enough information to be considered complete.
        """
        return 'complete' in response and response['complete']

    def generate_refinement_prompt(self, response: dict) -> str:
        """
        Generate a prompt to request more information from the user.
        """
        return (
            "It seems we need more details to generate the API specification. "
            "Could you provide more information on the following aspects: "
            f"{response.get('missing_details', 'Please specify the endpoints, methods, and data models.')}"
        )

    def process_full_response(self, response: dict) -> dict:
        """
        Process and return the full response.
        """
        return {
            "status": "success",
            "data": response['api_specification']
        }
