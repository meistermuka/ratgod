import random

class RatGodBot:

    RAT_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ("Flipping a coin \n\n")
        },
    }

    def __init__(self, channel):
        self.channel = channel

    def _flip_coin(self):
        rand_int = random.randint(0,1)
        if rand_int == 1:
            results = "Tails"
        else:
            results = "Heads"

        text = f"The result is {results}"

        return {
            "type": "section", 
            "text": {
                "type": "mrkdwn",
                "text": text
                }
            }

    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.RAT_BLOCK,
                #*self._flip_coin(),
            ],
        }