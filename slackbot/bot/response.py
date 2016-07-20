"""
A bot that sends a message if a given word appears in a message
"""

from .abc import SlackBot
from .util import has_text, text_contains


class ResponseBot(SlackBot):
    def __init__(self, *, word, response):
        self.word = word
        self.response = response

    def parse(self, message):
        if has_text(message):
            if text_contains(message, self.word):
                return ()

    def do(self, client, message, args):
        channel = message['channel']
        client.rtm_send_message(channel=channel, message=self.response)
