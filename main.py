import aiogram
import test1
import pprint

from aiogram import types, executor
from aiogram import Bot, Dispatcher

from pprint import pformat


token = '6087130044:AAGZuZ6DKZcMemELYHaQlyhM4dhr-opBPGs'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    result = await (test1.extract())
    await message.answer(pprint.pformat(result))

@dp.message_handler(commands=['test'])
async def on_test(message: types.Message):
    await message.answer('test!')

executor.start_polling(dp, skip_updates=True)