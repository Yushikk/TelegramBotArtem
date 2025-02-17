import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from config import TOKEN
from handlers import router

bot = Bot(token=TOKEN)
db = Dispatcher()


async def main():
    db.include_router(router)
    await db.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='help', description='Помощь с командами'),
                BotCommand(command='show', description='Показать список дел'),
                BotCommand(command='add', description='Добавить дело'),
                BotCommand(command='clear', description='Удалить абсолютно все дела за конкретный день')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
