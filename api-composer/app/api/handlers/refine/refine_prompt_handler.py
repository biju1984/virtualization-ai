from app.api.handlers.base_handler import Handler

class RefinePromptHandler(Handler):
    def handle(self, request):
        # Logic to refine the prompt
        request['refined_prompt'] = "Refined: " + request['prompt']
        return super().handle(request)
