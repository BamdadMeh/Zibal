from abc import ABC, abstractmethod
from requests import Response


class _Medium(ABC):

    @abstractmethod
    def send(self, message, receiver) -> Response:
        pass
