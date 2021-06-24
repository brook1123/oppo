# LINE聊天機器人

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('WSL + MBZe6fbpYtnmP / olujyZ4G / QqlgvKSvtQ + PfhLZaJxiZwMpB2Rn35Zi / BcFKOnJQlVbjMSaQzKqXsdcKM46Eo0u0ODDTelOESeNB2cet7xOM + yrJdlDTQCQIu943oSAbmgKXKN3pcdVBW6QBYgdB04t89 / 1O / w1cDnyilFU =')
handler = WebhookHandler('71fef19e7a9f97da6c9c36d73b828c28')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

