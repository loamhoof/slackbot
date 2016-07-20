#!/usr/bin/python3

import command.api as api
from slackbot.bot.command import CommandBot
from slackbot.bot.response import ResponseBot
from slackbot.bot.useremoji import UserEmojiBot
from slackbot.bot.wordemoji import WordEmojiBot
from slackbot.client import run


TOKEN = 'xxxxx'
BOT_ID = 'xxxxx'
MY_ID = 'xxxxx'


def main():
    bot = CommandBot(bot_id=BOT_ID, name='do', args=('some', 'thing'), command=api.firstcommand) \
        | CommandBot(bot_id=BOT_ID, name='or', args=('some', 'thing', 'else'), command=api.secondcommand) \
        | (UserEmojiBot(user=MY_ID, emoji='troll')
            & WordEmojiBot(word='dude', emoji='feelsgood')
            & WordEmojiBot(word='cow', emoji='cow')
            & (WordEmojiBot(word='airplane', emoji='airplane') | WordEmojiBot(word='superman', emoji='airplane'))
            & (UserEmojiBot(user=MY_ID, emoji=None) > WordEmojiBot(word='cake', emoji='hungry'))
            & ResponseBot(word='doge', response='wow'))
    run(token=TOKEN, bot=bot)


if __name__ == '__main__':
    main()
