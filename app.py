from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    TemplateMessage,
    ButtonsTemplate,
    PostbackAction
)
from linebot.v3.webhooks import (
    MessageEvent,  # 訊息
    FollowEvent,   # 加入或刪除帳號
    UnfollowEvent,
    PostbackEvent, # 用戶點擊按鈕
    TextMessageContent
)
import os

# todo 試著把邏輯分類出去
app = Flask(__name__)

# 從 .env 撈敏感資訊
zzo_access_token = os.getenv('LINE_ACCESS_TOKEN')
zzo_channel_secret = os.getenv('LINE_CHANNEL_SECRET')

# 檢查環境變數是否正確設置
if not zzo_access_token or not zzo_channel_secret:
    raise ValueError("LINE_ACCESS_TOKEN or LINE_CHANNEL_SECRET is not set in environment variables")

# access_token 是 line channel 的存取碼
configuration = Configuration(access_token=zzo_access_token)
# 使用 webhook 監聽 channel 需要用到 Channel secret
handler = WebhookHandler(zzo_channel_secret)

# 這個是 post 方法, 路徑action是/callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        # 接收到不同的 event 會在這邊分給不同的 action
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 當 event 是 MessageEvent 這邊做事情
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:        
        line_bot_api = MessagingApi(api_client)
        # 2. 當輸入特定文字, 回傳postback讓用戶點擊
        if event.message.text == '優惠':
            button = ButtonsTemplate(
                title='XXX優惠',
                text='領取優惠',
                actions=[ # text 是 點擊後領取的字
                    PostbackAction(label='領取優惠', text='已領取優惠', data='GetCoupon')
                ]
            )
            template_message = TemplateMessage(
                altText='領優惠altText',
                template=button
            )
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[template_message]
                )
            )
        else:
            # 1. 直接回傳echo範例
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token, # 這是用戶傳訊息來的時候, 會附上的 reply token
                messages=[TextMessage(text=event.message.text)]
            ))

@handler.add(PostbackEvent)
def handel_postback(event):
    if event.postback.data == 'GetCoupon':
        print(f'用戶{event.source.user_id}領優惠')

# 加入好友事件
@handler.add(FollowEvent)
def handel_follow(event):
    print(f'Got {event.type} event')

# 被封鎖事件
@handler.add(UnfollowEvent)
def handel_unfollow(event):
    print(f'Got {event.type} event')


if __name__ == "__main__":
    app.run()