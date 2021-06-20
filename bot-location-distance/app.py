from flask import Flask, request, abort
import json
import genflex
import distancecalculate
import os
from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage,FlexSendMessage
)

app = Flask(__name__)
#line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
#handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

line_bot_api = LineBotApi('31qfrDJDMECWXHNM8C/PZCxTyvJIqMl5iRbKSC0/OD5uThzEcESwKIIo1UhNqWi9BlCtSEVhydUK97n6R5yUY4GgZjerHlEkbZ8Bi9wlwJsyETi917wAZr1MX+Cc/hAPYmr5MmsjEHj1TiNA7MZkdgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e9b9372748ebfa3eda9dd558372e9c62')

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

@handler.add(MessageEvent)
def handle_message(event):
	type = event.message.type
	if type == 'location':
		longitude = event.message.longitude
		latitude = event.message.latitude
		dthome = distancecalculate.calculate(latitude,longitude)
		if(len(dthome) == 0):
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text="ไม่พบข้อมูล"))
		else:
			resultobj = genflex.flexobj(dthome)
			message = FlexSendMessage(alt_text="ข้อมูลบ้าน", contents=resultobj)
			line_bot_api.reply_message(event.reply_token,message)
	else:
		flexobj = genflex.flexagain()
		message = FlexSendMessage(alt_text="โปรดส่งตำแหน่งที่ตั้ง", contents=flexobj)
		line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
	#app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)