from app.api.handlers.base_handler import Handler
from app.services.openai_service import OpenAIService


class OpenAIHandler(Handler):
    def handle(self, request):
        try:
            response = OpenAIService().generate_specification(
                request['description'])
            if not response:
                raise ValueError("OpenAI returned an empty response")
            request['openai_response'] = response
            return super().handle(request)
        except Exception as e:
            request['error'] = str(e)
            return request  # End the chain if there's an error
