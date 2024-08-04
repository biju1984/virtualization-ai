from app.api.handlers.base_handler import Handler
from app.services.prompt_service import handle_prompt

class OpenAIHandler(Handler):
    def handle(self, request):
        response = handle_prompt(request.prompt)
        request.update(response)
        return super().handle(request)
