from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging

load_dotenv()
API_TOKEN =  os.getenv("TELEGRAM_BOT_TOKEN")

#configure logging

logging.basicConfig(level=logging.INFO)

#Initialize bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi!\n I am an Echo Bot!\n Powered by Aiogram")

## 在 Telegram 中可以輸入 `/start` 或 `/help` 測試


@dp.message_handler()
async def echo(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply(message.text)
## 在 Telegram 中可以輸入 任意字串 測試

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)