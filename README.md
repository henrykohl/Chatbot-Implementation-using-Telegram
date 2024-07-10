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


* 建立 `reseach/echo_bot.py`
> ```bash
> python research/echo_bot.py

* 建立 `my_bot.py`
> 執行 `my_bot.py` 以做任何測試時，以下需要先完成
> ```python
> if __name__ == "__main__":
>    executor.start_polling(dispatcher, skip_updates=True)
> ```