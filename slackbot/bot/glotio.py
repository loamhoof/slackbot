"""
A bot that executes snippets on glot.io
"""
import json

import requests

from .abc import SlackBot
from .util import is_snippet, snippet_title_contains


class GlotioBot(SlackBot):
    def __init__(self, token):
        self.token = token

    def parse(self, message):
        if is_snippet(message) is True and snippet_title_contains(message, 'exec'):
            return ()

    def do(self, client, message, args):
        snippet = client.api_call('files.info', file=message['file']['id'])['content']

        language = message['file']['filetype']
        response = requests.post(
            url='https://run.glot.io/languages/%s/latest' % language,
            headers={
                'Authorization': 'Token %s' % self.token,
                'Content-type': 'application/json',
            },
            data=json.dumps({
                'files': [{
                    'name': 'main.%s' % language,
                    'content': snippet,
                }],
            }),
        )

        if response.status_code == 200:
            result = response.json()
            client.rtm_send_message(
                channel=message['channel'],
                message='\n'.join((
                    'error:',
                    '%(error)s',
                    'stderr:',
                    '%(stderr)s',
                    'stdout:',
                    '%(stdout)s',
                )) % result
            )
