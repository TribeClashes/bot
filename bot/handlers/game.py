from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.filters.group import IsGroup
from bot.filters.private import IsPrivate

game_command_router: Router = Router(name=__name__)


@game_command_router.message(Command("game"), IsPrivate())
async def on_private_game_command(message: Message) -> None:
    await message.reply("<i>This command is only available in groups</i>")


@game_command_router.message(Command("game"), IsGroup())
async def on_group_game_command(message: Message) -> None:
    pass
