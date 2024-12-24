from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiohttp import ClientSession

from bot.assets.managers.game_manager import GameManager
from bot.assets.request_manager import RequestManager


class RequestsMiddleware(BaseMiddleware):
    def __init__(
            self,
            base_url: str,
            *,
            headers: Dict[str, str] | None = None
    ) -> None:
        self.base_url: str = base_url
        self.headers: Dict[str, str] = headers or {}

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        request_manager: RequestManager = RequestManager(self.base_url, headers=self.headers)

        async with ClientSession() as session:
            request_manager.inject_session(session)
            data.update(
                {
                    "rm": request_manager,
                    "games": GameManager(request_manager)
                }
            )

            return await handler(event, data)
