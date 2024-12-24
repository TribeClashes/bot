from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.assets.game import Game
from bot.assets.managers.game_manager import GameManager
from bot.exceptions.already_exists_error import AlreadyExistsError
from bot.filters.group import IsGroup
from bot.filters.private import IsPrivate

game_command_router: Router = Router(name=__name__)


@game_command_router.message(Command("game"), IsPrivate())
async def on_private_game(message: Message) -> None:
    await message.reply("<i>This command is only available in groups</i>")


@game_command_router.message(Command("game"), IsGroup())
async def on_group_game(
        message: Message,
        games: GameManager
) -> None:
    try:
        game: Game = await games.create(message.chat.id)
    except AlreadyExistsError:
        await message.reply("<i>Game already exists</i>")
        return

    await message.reply("<i>gol</i>")
