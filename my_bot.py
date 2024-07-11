from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import openai


load_dotenv()
API_TOKEN =  os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")


openai.api_key = OPENAI_API_KEY

# print("Ok")

MODEL_NAME = "gpt-3.5-turbo"


#Initialize bot
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


class Reference:
    def __init__(self) -> None:
        self.response = ""

"""
在 ChatGPT 中 ，不是在 Telegram 中
輸入： give me a python code to add 2 numbers
再輸入： i need without using function
"""

reference = Reference()

def clear_past():
    reference.response = ""



@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi\nI am a Chat Bot! Created by Bappy. How can i assist you?")

"""
在Telegram中輸入 `/start`
"""

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm a bot created by Bappy! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)

"""
在Telegram中輸入 `/help`
"""


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

"""
在Telegram中輸入 `/clear` ，用以清除記憶
"""



@dispatcher.message_handler()
async def main_bot(message: types.Message):
    """
    A handler to process the user's input and generate a response using the openai API.
    """

    print(f">>> USER: \n\t{message.text}")

    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    """old style(Lecture)"""
    # await bot.send_message(chat_id = message.chat.id, text = reference.response)
    """new style(my test)"""
    await message.answer("GPT answer:"+reference.response)

"""
在 Telegram 輸入：
hi
tell me about python
give me a python code to add 2 numbers
i need with using function
/clear
hi
"""    

## 執行 my_bot.py 做任何測試時，以下需要先完成
if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)



