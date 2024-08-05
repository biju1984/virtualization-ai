from app.api.handlers.base_handler import Handler
from app.services.openai_service import generate_api_specification


class OpenAIHandler(Handler):
    def handle(self, request):
        response = generate_api_specification(request['description'])
        request['openai_response'] = response
        return super().handle(request)
