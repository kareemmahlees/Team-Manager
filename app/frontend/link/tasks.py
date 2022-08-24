import requests
from requests.models import Response
from ..core.config import settings


class Tasks(requests.Session):
    def __init__(self) -> None:
        super().__init__()

    def get_tasks(self) -> Response:
        res = self.get(f"{settings.api_url}/task/all")
        return res
