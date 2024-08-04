from app.api.handlers.base_handler import Handler
from app.services.api_service import save_specification

class SaveSpecificationHandler(Handler):
    def handle(self, request):
        # Logic to save the specification
        spec_id = save_specification(request['name'], request['description'], request['spec_type'], request['spec'])
        request['spec_id'] = spec_id
        return super().handle(request)
