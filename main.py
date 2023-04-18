import aiogram

from aiogram import types, executor
from aiogram import Bot, Dispatcher

from pprint import pformat


token = '6087130044:AAGZuZ6DKZcMemELYHaQlyhM4dhr-opBPGs'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    result = await parse_dota2_matches()
    s = ''
    for value in result.values():
        for team, fact in value.items():
            s += '{0} - {1} |'.format(team, fact)
        s += '\n'
    await message.answer(s[:4000])

@dp.message_handler(commands=['test'])
async def on_test(message: types.Message):
    await message.answer('test!')

def on_shutdown(arg):
    driver.quit()

executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)