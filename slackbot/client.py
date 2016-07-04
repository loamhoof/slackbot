"""
Wrap the slackclient to run a bot
"""

from time import sleep

from slackclient import SlackClient

from .error import ConnectionError


def run(*, token, bot, frequency=1):
    client = SlackClient(token)

    if not client.rtm_connect():
        raise ConnectionError

    # print(client.api_call('users.list'))

    while True:
        messages = client.rtm_read()

        for message in messages:
            parse_result = bot.parse(message)
            if parse_result is not None:
                bot.do(client, message, parse_result)

        sleep(frequency)
