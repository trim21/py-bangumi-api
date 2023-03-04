import httpx

from bangumi_api.error import NotFoundError
from bangumi_api.model import Subject


class Client:
    client: httpx.Client

    def __init__(self, token: str = None):
        headers = {"user-agent": 'py-bangumi-api/dev'}
        if token:
            headers.update({"authorization": f'Bearer {token}'})
        self.client = httpx.Client(
            base_url="https://api.bgm.tv/v0/",
            follow_redirects=True,
            headers=headers
        )

    @staticmethod
    def _raise_for_status(r: httpx.Response):
        if r.is_success:
            return

        if r.status_code == 404:
            raise NotFoundError(r.url)

        r.raise_for_status()

    def get_subject(self, subject_id: int) -> Subject:
        r = self.client.get(f"subjects/{subject_id}")
        self._raise_for_status(r)

        return Subject.parse_obj(r.json())
