from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm a bot created with aiogram on Cloudflare Workers.")