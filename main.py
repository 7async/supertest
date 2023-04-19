import aiogram
import test1
import pprint
import time
import asyncio

from aiogram import types, executor
from aiogram import Bot, Dispatcher

from collections import defaultdict
from pprint import pformat


token = '6087130044:AAGZuZ6DKZcMemELYHaQlyhM4dhr-opBPGs'
bot = Bot(token)
dp = Dispatcher(bot)

result = defaultdict(lambda: (1, 1))

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer(pprint.pformat(result) if result else 'Empty')

@dp.message_handler(commands=['test'])
async def on_test(message: types.Message):
    await message.answer('test!')

async def result_updating():
    global result
    while True:
        result.update(await (test1.extract()))
        result['TIME'] = time.strftime('%X')
        await asyncio.sleep(180)


loop = asyncio.get_event_loop()
loop.create_task(result_updating())

executor.start_polling(dp, skip_updates=True)