"""
A bot meant to be used as a console
"""

import shlex

from .abc import SlackBot
from .util import has_text, text_startswith


class CommandBot(SlackBot):
    def __init__(self, bot_id, name, args, command):
        self.bot_id = bot_id
        self.name = name
        self.args = args
        self.command = command

    def parse(self, message):
        if has_text(message) and text_startswith(message, r'<@%s>:? \w+' % self.bot_id):
            args = shlex.split(message['text'])[1:]
            if args[0] == self.name and len(args[1:]) == len(self.args):
                return args[1:]

    def do(self, client, message, args):
        channel = message['channel']
        try:
            client.rtm_send_message(channel=channel, message='Executing %s %s' % (self.name, self.args))
            self.command(**dict(zip(self.args, args)))
        except:
            client.rtm_send_message(channel=channel, message='Failure')
        else:
            client.rtm_send_message(channel=channel, message='Success')
