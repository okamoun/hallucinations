from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Subsession, Group,Player
from html.parser import HTMLParser
from gpt_tools import QueryWithCache,GPTBotDyna,ProfileToPromptUS
import logging
import pandas as pd


class PlayerBot(Bot,GPTBotDyna):
    pages_seq = pages.page_sequence

    cases = ['gpt']
    start_after=0
    ptp = ProfileToPromptUS(profile_seq=["sex", "age",
                                         "last_elect",
                                         "educ",
                                         "religion"   ,'residence','ownhome'
                                         ])
    use_profile = True


