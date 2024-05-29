from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Subsession, Group,Player
from html.parser import HTMLParser
from gpt_tools import ProfileToPromptKT,GPTSoup,GPTBotDyna
import logging
import pandas as pd



class PlayerBot(Bot,GPTBotDyna):
    pages_seq = pages.page_sequence

    cases = ['gpt']
    ptp = ProfileToPromptKT()
    use_profile = True
    profile_file ='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/kt_propect/data/modified_exclusions/pt_replication_modified_exclusions_data_shuffled.csv'

    prompt_template = 'create json to fill the html form to maximize your gain, do not leave any filed empty or blanc, return only the json no comment :  {myhtml}'


    def get_profile_id_unique(self):
        return 1

    def play_round(self):
        if self.case =='gpt':
            #yield result from parent method
            yield from super().play_round()
