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
    await message.reply(f'Привет! {user_name}! Пришли мне фотографию бутылки и я скажу тебе что это за пиво')

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await message.photo[-1].download("input.jpg", make_dirs=False)
    await message.answer('Фото принял, ищу пиво')
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await asyncio.sleep(4)
    get_prediction()
    result = getinfo()
    if result == 'Я не вижу пиво':
        await message.answer('Я не вижу пиво')
    else:
        name, style, ABV, IBU, rating, description  = result
        answer = f'Вот что я нашел: \n<b>{name}</b> \n<b>Стиль</b>: {style} \n<b>Оценка</b>: {rating} из 5 \n<b>Крепость</b>: {ABV} \n<b>Плотность</b>: {IBU}'
        await message.answer(answer, parse_mode = 'HTML')

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.reply('Пока я умею определять пиво только по одному фото, так что пожалуйста, не присылайте мне больше одной фотографии за раз. Желательно, чтобы бутылка или банка занимали большую часть кадра. Мой сервер не самый дорогой, поэтому на ответ мне нужно в среднем 10 секунд.')

@dp.message_handler()
async def start(message: types.Message):
    await message.reply('Я умею гадать только по фото')

if __name__ == '__main__': #всегда тру
    executor.start_polling(dp)