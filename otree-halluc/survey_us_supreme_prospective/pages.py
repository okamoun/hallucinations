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

class Past(Page):
    form_model = 'player'
    form_fields = ['influence_society', 'influence_like_you', 'open_ended_past']

    def vars_for_template(self):

        player = self.player
        influence_society_label_dict =  {"B":"benefits","H":"harms","I":"influences"}
        return dict(
            influence_society_label = f'In general, how do you think SOCIETY has been influenced by decisions of the Supreme Court in the past {player.time_frame_past} years? ',
            influence_like_you_label = f'In general, how do you think PEOPLE LIKE YOU have been influenced by decisions of the Supreme Court in the past {player.time_frame_past} years? ',
            player_time_frame_future=player.time_frame_future,
            player_influence_type=player.influence_type,
            options_influence=influence_society_label_dict,
            options_time_frame=str([15,75]))




class Future(Page):
    form_model = 'player'
    form_fields = ['future_influence_society', 'future_like_you', 'open_ended_future']



    def vars_for_template(self):
        player = self.player
        print(dir(player))
        print(dir(player.values_dicts))
        influence_society_label_dict={"B":"benefit from","H":"be hurt by","I":"be influenced by"}

        return dict(
            future_influence_society_label = f'How much do you think SOCIETY is likely to { influence_society_label_dict[player.influence_type] }  from decisions of the Supreme Court in the NEXT  {player.time_frame_future} years?  ',
            future_like_you_label = f'How much do you think PEOPLE LIKE YOU is likely to {influence_society_label_dict[player.influence_type] }  from decisions of the Supreme Court in the NEXT  {player.time_frame_future} years? ',
            player_time_frame_future=player.time_frame_future,
            player_influence_type=player.influence_type,
            options_influence=str(influence_society_label_dict),
            options_future_time_frame=str([15,75]))
    def app_after_this_page(self,upcoming_apps):
        #return reform only if reform is in the list of apps
        if 'reform' in upcoming_apps:
            return 'reform'
        else :
            return upcoming_apps[0]

class CourtDecision(Page):
    form_model = 'player'

    form_fields = ['court_decision']


class END(Page):
    form_model = 'player'



page_sequence = [Past, Future]