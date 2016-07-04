"""
A bot that adds a reaction emoji if a given word appears in a message
"""

from .abc import SlackBot
from .util import has_text, text_contains


class WordEmojiBot(SlackBot):
    def __init__(self, *, word, emoji):
        self.word = word
        self.emoji = emoji

    def parse(self, message):
        if has_text(message):
            if text_contains(message, self.word):
                return ()

    def do(self, client, message, args):
        client.api_call('reactions.add', channel=message['channel'], timestamp=message['ts'], name=self.emoji)
