from flask import Flask, request, abort
import requests
import json

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (MessageEvent,TextMessage,TextSendMessage)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('8qSieeqd0aSUL7iD9FzJEV8Rzzd1MSNT046pTO7w/7gf9lJBVxtIpAwJLs6FIJ8dz6ZjBED8muJdoXlP9lrDumWOeMnkKUj3qRchrEA2lfzrp0DAJMRzQdRKZbhU0lc4pnPZ1ciqyJilqt8l3AOs4AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f1487774e3dd859b806445e0a3218d5c')

@app.route("/qnamaker", methods=['POST'])
def get_answer(message_text):

    url = "https://ninatellyou.azurewebsites.net/qnamaker/knowledgebases/85010cbc-6cdf-4692-9647-f16054033d8e/generateAnswer"
    
    response = requests.post(
        url,
        json.dumps({'question': message_text}),
        headers={'Content-Type': 'application/json',
                'Authorization': 'e2c263e1-25ec-47c4-b8c1-df2a07cd98c0'
        }
        )

    data = response.json()

    try:
        if "error" in data:
            return data["error"]["message"]
        else:    
            answer = data['answers'][0]['answer']
            return answer
    except Exception:
        return "Error occurs when finding answer"


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

    
# 處理訊息

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    answer = get_answer(event.message.text)
    line_bot_api.reply_message(event.reply_token,
    TextSendMessage(text=answer))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
