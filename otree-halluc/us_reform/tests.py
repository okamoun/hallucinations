import logging

from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import C,choices_list
from gpt_tools import QueryWithCache,GPTBotDyna

class PlayerBot(Bot, GPTBotDyna):

    cases = ['gpt']

    pages_seq = pages.page_sequence



    inputs_cases= {'basic':{''}}

    def form_for_case(self,field_name,i,choice_list = choices_list):
        if field_name in choice_list:
            return choice_list[field_name][i % len(choice_list[field_name])]
        else :
            return '0'



    def play_round_old(self):
        if self.case >= self.start_after:
            for page in pages.page_sequence[0:self.case-self.start_after]:
                dform = {field_name:self.form_for_case(field_name,0,choices_list) for field_name in page.form_fields}
                print(dform)
                yield (page, dform)

    def play_round_MAN(selfs):
        yield (pages.Decisions,{'court_decision':'1-generally to the left'})
        yield (pages.Profile,  {'age': '0', 'political_ide': '1-very left wing', 'political_aff': '1-voted for a party not in the coalition', 'political_gov_sup': '1-Strongly Oppose', 'sex': '1-Male', 'status': '1-Foreign', 'educ': '1-Did not finish high school'})





