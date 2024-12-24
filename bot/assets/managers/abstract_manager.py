from abc import ABC, abstractmethod
from typing import TypeVar, Any

T = TypeVar("T")


class AbstractManager(ABC):
    @abstractmethod
    async def create(
            self,
            *args: Any,
            **kwargs: Any
    ) -> T | None:
        pass

    @abstractmethod
    async def get(
            self,
            uid: Any
    ) -> T | None:
        pass

    @abstractmethod
    async def remove(
            self,
            uid: Any
    ) -> None:
        pass
