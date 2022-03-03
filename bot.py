import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
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
    get_prediction()
    result = getinfo()
    await message.reply(str(result))


if __name__ == '__main__': #всегда тру
    executor.start_polling(dp)