import os
import logging

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from ratgodbot import RatGodBot

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)

slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

def flip_coin(channel):

    ratbot = RatGodBot(channel)

    message = ratbot.get_message_payload()

    slack_web_client.chat_postMessage(**message)

@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})
    text = event.get("text")

    if "something" in text.lower():
        channel_id = event.get("channel")

        return flip_coin(channel_id)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    app.run(host='0.0.0.0', port=5555)