from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return request
