from otree.api import *
from ._builtin import Page, WaitPage
from .models import C, Player
c = cu

doc = ''

def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]

class prospect_items(Page):
    form_model = 'player'

    def get_form_fields(self):
        item_s =  eval(self.player.item_seq)
        return [f"item_{i}" for i in item_s[:6]] +['item_20']


class prospect_items2(Page):
    form_model = 'player'

    def get_form_fields(self):
        item_s =  eval(self.player.item_seq)
        return [f"item_{i}" for i in item_s[6:]] #+['item_21']





page_sequence = [prospect_items, prospect_items2]