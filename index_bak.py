#-*- coding: utf-8 -*-　　 

from __future__ import print_function
import json
import os
import sys
from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerMessage, StickerSendMessage
)
#IBM Language Translator
from watson_developer_cloud import LanguageTranslatorV3

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = 'a8a677c1556cee2b391d9c9bf48e9886'
channel_access_token = 'M4p9wTXd1lVh1b/JEsZEWJYWh0moL6uNfTwyv2cSZHgGpAXgHKlwpMYi0sQOrHQTQnPxg2A5NKgFpJpKf7JX8HPnTmbl7XyCmBbnmk0dZ1gVsVBj4qCh8IvLjOuS70JafPpbQal89oWMKUT3XfUbGAdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

language_translator = LanguageTranslatorV3( version='2018-05-31', iam_api_key='tppoJc9atJQ6OdAxKowb--fobg3v37XBsctH9aN-hmxw')


# handle callback
@app.route("/")
def root():
    return 'HELLO'

@app.route("/translation")
def translation():
    request_message = "今天天氣很好".lower()
    language = language_translator.identify(request_message)
    print(json.dumps(language, indent=2))
    identify = language["languages"][0]["language"]
    response_message = '看不懂無法翻譯'
    if identify == 'zh' :
        response_message_json = language_translator.translate(text=request_message,model_id='zh-en')
        response_message = response_message_json["translations"][0]["translation"]
    elif identify == 'zh-TW' :
        response_message_json = language_translator.translate(text=request_message,model_id='zh-TW-en')
        response_message = response_message_json["translations"][0]["translation"]
    elif identify == 'en' :
        response_message_json = language_translator.translate(text=request_message,model_id='en-zh-TW')
        response_message = response_message_json["translations"][0]["translation"]
    return response_message

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):

    request_message = event.message.text.lower()
    language = language_translator.identify(request_message)
    identify = language["languages"][0]["language"]
    response_message = event.message.text

    if identify == 'zh' :
        response_message_json = language_translator.translate(text=request_message,model_id='zh-en')
        response_message = response_message_json["translations"][0]["translation"]
    elif identify == 'zh-TW' :
        response_message_json = language_translator.translate(text=request_message,model_id='zh-TW-en')
        response_message = response_message_json["translations"][0]["translation"]
    elif identify == 'en' :
        response_message_json = language_translator.translate(text=request_message,model_id='en-zh-TW')
        response_message = response_message_json["translations"][0]["translation"]
    line_bot_api.reply_message( event.reply_token, TextSendMessage(text=response_message) )


@handler.add(MessageEvent, message=StickerMessage)
def message_sticker(event):
    line_bot_api.reply_message( event.reply_token, StickerSendMessage(package_id=1, sticker_id=1) )
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)