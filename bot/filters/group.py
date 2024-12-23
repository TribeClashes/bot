from typing import Any

from aiogram.enums import ChatType
from aiogram.filters import Filter


class IsGroup(Filter):
    async def __call__(
            self,
            telegram_object: Any
    ) -> bool:
        if not hasattr(telegram_object, "chat"):
            return False

        return telegram_object.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
