import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.scene import SceneRegistry
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from pydantic import SecretStr

from bot.handlers.start import start_command_router
from bot.middlewares.logging import LoggingMiddleware
from config import Config

config: Config = Config(_env_file=".env")


def register_middlewares(dispatcher: Dispatcher):
    dispatcher.update.outer_middleware.register(LoggingMiddleware("tribeclashes"))


def include_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(
        start_command_router
    )


def register_scenes(dispatcher: Dispatcher):
    registry: SceneRegistry = SceneRegistry(dispatcher)


def create_dispatcher() -> Dispatcher:
    redis_dsn: SecretStr | None = config.redis_dsn

    if redis_dsn is None:
        storage: MemoryStorage = MemoryStorage()
    else:
        storage: RedisStorage = RedisStorage.from_url(redis_dsn.get_secret_value())

    new_dispatcher: Dispatcher = Dispatcher(storage=storage)

    register_middlewares(new_dispatcher)
    include_routers(new_dispatcher)
    register_scenes(new_dispatcher)

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
