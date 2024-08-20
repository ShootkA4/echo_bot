import asyncio
import logging
from aiogram import Bot, Dispatcher, types 
from aiogram.filters.command import Command
from aiogram.types import Message
logging.basicConfig(level=logging.INFO)
token_bot=""

async def echo(message: Message):
    await message.answer(message.text)



async def start():
    bot=Bot(token=token_bot)
    dp=Dispatcher()

    dp.message.register(echo)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__=='__main__':
    asyncio.run(start())

