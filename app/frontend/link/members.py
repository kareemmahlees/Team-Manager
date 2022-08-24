import requests
from requests.models import Response
from ..core.config import settings


class Members(requests.Session):
    """
    class for handling members data
    """

    def __init__(self) -> None:
        super().__init__()

    def get_all_members(self) -> Response:
        res = self.get(f"{settings.api_url}/member/all")
        return res
