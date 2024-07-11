# Chatbot-Implementation-using-Telegram

* 建立 virtual environment
> ```bash
> virtualenv llmapp --python=python3.8
>
> source ./llmapp/bin/activate
> ```

* 建立 `.gitignore`

* 建立 `.env`
> 在 `Telegram APP` 中 找到 `BotFather` 後，輸入 `/newbot`，再輸入 `youtubetestbot`，然後用 `youtubetest0425_bot` 當成 *username* ，就可以取得 token 序列號
> 
> 並可開啟 t.me/youtubetest0425_bot

* 建立 `requirements.txt`
> ```bash
> pip install -r requirements.txt
> ```
> 注意，openai使用 0.28.1，如果使用最新版 openai >=1.0.0 ，在`my_bot.py` 中  openai 使用方式將有所不一樣
> 
> 舉例1--使用openai=0.28.1 
> ```python
> import openai
> 
> openai.api_key="..."
> openai.ChatCompletion.create()
> ```
> 舉例2--使用openai>=1.0.0
> ```python 
> from openai import OpenAI
>
> client = OpenAI(api_key="...")
> client.chat.completions.create()
> ```

* [aiogram 2.5 參考文件 (documentation)](https://docs.aiogram.dev/en/v2.25.1/quick_start.html)
> [aiogram 最新版參考文件]  (https://docs.aiogram.dev/en/latest/)

* 建立 `reseach/echo_bot.py`
> ```bash
> python research/echo_bot.py

* 建立 `my_bot.py`
> 執行 `my_bot.py` 以做任何測試時，以下需要先完成
> ```python
> if __name__ == "__main__":
>    executor.start_polling(dispatcher, skip_updates=True)
> ```