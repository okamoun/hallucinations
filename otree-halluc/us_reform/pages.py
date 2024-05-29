from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import C


class Court_knowledge(Page):
    form_model = 'player'
    form_fields = ['court_knowledge', 'court_interest', 'court_interst_since']

class CourtDecision(Page):
    form_model = 'player'
    form_fields = ['court_decision']
    def is_displayed(self):
        if self.player.session.config['name']!='IsraelCourtProspective' :
            self.pages_excluded=[self.__class__.__name__]
            return False
        else:
            return True

class Changes(Page):
    form_model = 'player'
    form_fields = ['changes']
class Changes_specifics(Page):
    form_model = 'player'
    form_fields = ['change_term', 'change_selection', 'change_size']

class Thanks(Page):
    form_model = 'player'
page_sequence = [Changes,Changes_specifics]

