import logging
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class LoggingMiddleware(BaseMiddleware):
    def __init__(
            self,
            name: str,
            *,
            level: int = logging.INFO
    ) -> None:
        self.name: str = name

        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        data["logger"] = self.logger
        return await handler(event, data)
