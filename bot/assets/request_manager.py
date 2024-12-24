import asyncio
import logging
from typing import Dict, Callable, Any

from aiohttp import ClientSession, ClientConnectorError

from bot.exceptions.server_error import ServerError
from bot.utils.attributed_dict import AttributedDict


class RequestManager:
    def __init__(
            self,
            base_url: str,
            *,
            headers: Dict[str, str] | None = None
    ) -> None:
        self.base_url: str = base_url
        self.headers: Dict[str, str] | None = headers or {}

        self.session: ClientSession | None = None

    def inject_session(
            self,
            session: ClientSession
    ) -> None:
        self.session = session

    @staticmethod
    def __retry(
            function: Callable,
            *,
            retry_amount: int = 3,
            poll_timeout: int | float = 1
    ) -> Callable:
        async def wrapper(*args, **kwargs) -> AttributedDict | None:
            for i in range(retry_amount):
                try:
                    return await function(*args, **kwargs)
                except ClientConnectorError as error:
                    if i < retry_amount - 1:
                        logging.getLogger("tribeclashes").warning(
                            f"Error occurred while connecting to server: {error}"
                        )
                        await asyncio.sleep(poll_timeout)

            logging.getLogger("tribeclashes").error(
                f"Retry amount reached while connecting to server"
            )
            raise ServerError

        return wrapper

    @__retry
    async def post(
            self,
            path: str,
            *,
            headers: Dict[str, str] | None = None,
            params: Dict[str, Any] | None = None,
            data: Dict[str, Any] | None = None
    ) -> AttributedDict:
        async with self.session.post(
                f"{self.base_url}/{path}",
                headers=self.headers | (headers or {}),
                params=params,
                data=data
        ) as response:
            json: Dict[str, Any] = await response.json()

            json.update(
                {
                    "status_code": response.status
                }
            )

            return AttributedDict(json)

    @__retry
    async def get(
            self,
            path: str,
            *,
            headers: Dict[str, str] | None = None,
            params: Dict[str, Any] | None = None,
            data: Dict[str, Any] | None = None
    ) -> AttributedDict:
        async with self.session.get(
                f"{self.base_url}/{path}",
                headers=self.headers | (headers or {}),
                params=params,
                data=data
        ) as response:
            json: Dict[str, Any] = await response.json()

            json.update(
                {
                    "status_code": response.status
                }
            )

            return AttributedDict(json)

    @__retry
    async def delete(
            self,
            path: str,
            *,
            headers: Dict[str, str] | None = None,
            params: Dict[str, Any] | None = None,
            data: Dict[str, Any] | None = None
    ) -> AttributedDict:
        async with self.session.delete(
                f"{self.base_url}/{path}",
                headers=self.headers | (headers or {}),
                params=params,
                data=data
        ) as response:
            json: Dict[str, Any] = await response.json()

            json.update(
                {
                    "status_code": response.status
                }
            )

            return AttributedDict(json)
