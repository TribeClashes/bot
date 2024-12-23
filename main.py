import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import Config

config: Config = Config(_env_file=".env")


def create_dispatcher() -> Dispatcher:
    new_dispatcher: Dispatcher = Dispatcher()
    return new_dispatcher


async def main() -> None:
    bot: Bot = Bot(
        token=config.telegram_bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dispatcher: Dispatcher = create_dispatcher()

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
