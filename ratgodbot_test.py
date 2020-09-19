from slack import WebClient
from ratgodbot import RatGodBot

import os

slack_web_client =  WebClient(token=os.environ.get("SLACK_TOKEN"))

rat_bot = RatGodBot("#random")

message = rat_bot.get_message_payload()

slack_web_client.chat_postMessage(**message)
