from app.api.handlers.base_handler import Handler
# You need to implement this
from app.services.specification_service import save_specification


class SaveSpecificationHandler(Handler):
    def handle(self, request):
        spec_id = save_specification(request['refined_response'])
        request['spec_id'] = spec_id
        return super().handle(request)
