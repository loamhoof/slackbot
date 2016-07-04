"""
A bot that adds a reaction emoji if a given user sends a message
"""

from .abc import SlackBot
from .util import from_user, has_text


class UserEmojiBot(SlackBot):
    def __init__(self, *, user, emoji):
        self.user = user
        self.emoji = emoji

    def parse(self, message):
        if has_text(message) and from_user(message, self.user):
            return ()

    def do(self, client, message, args):
        client.api_call('reactions.add', channel=message['channel'], timestamp=message['ts'], name=self.emoji)
