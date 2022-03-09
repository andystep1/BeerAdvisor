import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ChatActions
from config import TOKEN
from functions import get_prediction, getinfo


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    await message.reply(f'Привет! {user_name}!')

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await message.photo[-1].download("input.jpg", make_dirs=False)
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await asyncio.sleep(3)
    get_prediction()
    if getinfo() == 'Я не вижу пиво':
        await message.answer('Я не вижу пиво')
    else:
        name, style, ABV, IBU, rating, description  = getinfo()
        await message.answer(name)
        await message.answer(style)
        await message.answer(ABV)
        await message.answer(IBU)
        await message.answer(rating)
        #await message.answer(description)


if __name__ == '__main__': #всегда тру
    executor.start_polling(dp)