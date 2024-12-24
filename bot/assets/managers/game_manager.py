from starlette import status

from bot.assets.game import Game
from bot.assets.managers.abstract_manager import AbstractManager
from bot.assets.request_manager import RequestManager
from bot.exceptions.already_exists_error import AlreadyExistsError
from bot.exceptions.not_found_error import NotFoundError
from bot.utils.attributed_dict import AttributedDict


class GameManager(AbstractManager):
    def __init__(
            self,
            request_manager: RequestManager
    ) -> None:
        self.request_manager: RequestManager = request_manager

    async def create(
            self,
            chat_id: int
    ) -> Game:
        response: AttributedDict = await self.request_manager.post(f"games/{chat_id}")

        if response.status_code == status.HTTP_409_CONFLICT:
            raise AlreadyExistsError

        return Game.from_response(response)

    async def get(
            self,
            chat_id: int
    ) -> Game:
        response: AttributedDict = await self.request_manager.get(f"games/{chat_id}")

        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise NotFoundError

        return Game.from_response(response)

    async def remove(
            self,
            chat_id: int
    ) -> None:
        await self.request_manager.delete(f"games/{chat_id}")
