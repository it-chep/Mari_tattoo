import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

from config import Bot_Token


bot = Bot(token=Bot_Token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

web_app_btn = WebAppInfo(url='https://1305-2a0d-5600-41-b000-00-7454.ngrok-free.app')
btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Сайт', web_app=web_app_btn)]
    ]
)
'''
https://0b31-2605-6440-4010-00-84fc.ngrok.io
'''


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот!", reply_markup=btn)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

