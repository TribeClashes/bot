from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.filters.group import IsGroup
from bot.filters.private import IsPrivate

start_command_router: Router = Router(name=__name__)


@start_command_router.message(CommandStart(), IsPrivate())
async def on_private_start_command(message: Message) -> None:
    await message.reply(f"<b>Hello, {message.from_user.first_name}!</b>")


@start_command_router.message(CommandStart(), IsGroup())
async def on_group_start_command(message: Message) -> None:
    await message.reply(f"<b>Hello, {message.chat.title}!</b>")
