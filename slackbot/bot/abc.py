"""
Bot abc
Mainly some operators overloading to combine bots
"""

import abc


class SlackBot(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse():
        pass

    @abc.abstractmethod
    def do():
        pass

    def __and__(bot1, bot2):
        def parse(self, message):
            parse_results = (
                bot1.parse(message),
                bot2.parse(message),
            )

            if parse_results != (None, None):
                return parse_results

        def do(self, client, message, args):
            if args[0] is not None:
                bot1.do(client, message, args[0])
            if args[1] is not None:
                bot2.do(client, message, args[1])

        return type(
            '%sAnd%s' % (bot1.__class__.__name__, bot2.__class__.__name__),
            (SlackBot,),
            dict(parse=parse, do=do)
        )()

    def __or__(bot1, bot2):
        def parse(self, message):
            for bot in (bot1, bot2):
                parse_result = bot.parse(message)
                if parse_result is not None:
                    return (bot, parse_result)

        def do(self, client, message, args):
            args[0].do(client, message, args[1])

        return type(
            '%sOr%s' % (bot1.__class__.__name__, bot2.__class__.__name__),
            (SlackBot,),
            dict(parse=parse, do=do)
        )()

    def __gt__(bot1, bot2):
        def parse(self, message):
            parse_results = (
                bot1.parse(message),
                bot2.parse(message),
            )

            if None not in parse_results:
                return parse_results[1]

        def do(self, client, message, args):
            bot2.do(client, message, args)

        return type(
            '%sGt%s' % (bot1.__class__.__name__, bot2.__class__.__name__),
            (SlackBot,),
            dict(parse=parse, do=do)
        )()
