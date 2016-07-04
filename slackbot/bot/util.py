"""
Some helpers on message manipulationtext_startswith
"""

import re


def has_text(message):
    return 'type' in message and message['type'] == 'message' and 'text' in message


def text_contains(message, word):
    return re.search(r'\b%s\b' % word, message['text'], re.I) is not None


def text_startswith(message, regex):
    return re.match(regex, message['text']) is not None


def from_user(message, user):
    return 'user' in message and message['user'] == user
