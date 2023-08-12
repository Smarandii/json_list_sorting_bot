from aiogram import \
    Bot, \
    Dispatcher
import os
from dotenv import \
    load_dotenv
from aiogram import types
from aiogram.dispatcher import filters

from coupon_sorting import save_as_json, save_as_string

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(filters.Command("start"))
async def start_cmd_handler(message: types.Message):
    await message.answer("Hello! Send me a json list to reorder!")


@dp.message_handler()
async def reorder_list_handler(message: types.Message):
    file_name = save_as_json(message.text)
    await bot.send_document(message.from_user.id, open(file_name, "rb"))

    json_string = save_as_string(file_name)
    await bot.send_message(message.from_user.id, json_string)


if __name__ == '__main__':
    from aiogram import executor
    while True:
        try:
            executor.start_polling(dp)
        except Exception as e:
            bot.send_message(chat_id=231584958, text=f'Bot has been stopped\n{e.args}')