from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from reguest import reguest

from loader import dp

@dp.message_handler(Command('check'))
async def bot_check(message: types.Message):
    await message.answer("Checking")