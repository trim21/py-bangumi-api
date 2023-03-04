from typing import Any

from httpx import URL


class Error(Exception):
    def __init__(self, url: URL, res: Any):
        self.url = url
        self.res = res
        super().__init__(res)


class UnauthorizedError(Error):
    status = 401


class NotFoundError(Error):
    status = 404
