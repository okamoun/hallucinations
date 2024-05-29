from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import C,choices_list
from gpt_tools import QueryWithCache,GPTSoup,GPTBotDyna,ProfileToPromptUS






class PlayerBot(Bot,GPTBotDyna):
    pages_seq = pages.page_sequence

    cases = ['gpt']

    use_profile = True

    ptp = ProfileToPromptUS()
    inputs_cases= {'basic':{''}}


