from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Zeyu Qiu'

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'survey_supreme_prospective_us'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    def creating_session(self):
        import random
        for player in self.get_players():
                player.time_frame_past = random.choice([15, 75])
                player.time_frame_future = random.choice([15, 75])
                player.influence_type = random.choice(['H','I','B'])
                player.specific_decision = random.choice(['Speech', 'Movement', 'Reasonableness','CG','Speech', 'Movement', 'Reasonableness',])



class Group(BaseGroup):
    pass

def double_list(l):
    return [[i,i] for i in l ]

def future_influence_society_choices(player):
    if player.influence_type=='H':
        return  [  '1-been hurt a great deal' , '2-been hurt somewhat ','3-been hurt slightly','4-not really influenced ','5-benefited slightly','6-benefited somewhat','7-benefited a great deal', '4-not really influenced']
    else :
        return  player.choice_future_list


class Player(BasePlayer):
    choice_past_list = (['1-benefited a great deal','1-benefited a great deal'], ['2-benefited somewhat','2-benefited somewhat'], ['3-benefited slightly','3-benefited slightly'], ['4-not really influenced','4-not really influenced'], ['5-been hurt slightly','5-been hurt slightly'], ['6-been hurt somewhat','6-been hurt somewhat'], ['7-been hurt a great deal','7-been hurt a great deal'])
    choice_future_list = ('1-likely to be substantially better off', '2-likely to be somewhat better off',
                          '3-likely to be slightly better off', '4-likely to be slightly worse off',
                          '5-likely to be somewhat worse off', '6-likely to be substantially worse off')

    choice_support_list = (['1-strongly support','1-strongly support'], ['2-somewhat support','2-somewhat support'], ['3-slightly support','3-slightly support'], ['4-slightly oppose ','4-slightly oppose '], ['5-somewhat oppose ','5-somewhat oppose '], ['6-strongly oppose','6-strongly oppose'])
    choice_decision_quality = ('1-Horrible Decision','2-Very Bad Decision','3-Bad Decision','4-Neutral','5-Good Decision','6-Very Good Decision','7-Excellent Decision')
    influence_society = models.StringField(choices= choice_past_list, label='In general, how do you think SOCIETY has been influenced by decisions of the Supreme Court in the past [75 / 15] years? ', widget=widgets.RadioSelect)
    influence_like_you = models.StringField(choices=choice_past_list, label='Specifically, how do you think PEOPLE LIKE YOU have been influenced by decisions of the Israeli Supreme Court over the past XX years? ',  widget=widgets.RadioSelect)
    open_ended_past = models.LongStringField(blank=True,label='In a sentence or two can you please indicate what you see as the MOST IMPORTANT impact that the court has made over this period?')
    future_influence_society = models.StringField( label='dyna', widget=widgets.RadioSelect)
    future_like_you = models.StringField(choices= choice_future_list , label='dyna ', widget=widgets.RadioSelect)
    open_ended_future = models.LongStringField(blank=True,label='In a sentence or two can you please indicate what you see as the MOST IMPORTANT influence that the court will have over this period?')

    court_decision = models.StringField(choices=[['1-generally to the left ', '1-generally to the left'], ['2-generally to the right', '2-generally to the right'], ['3-case by case basis', '3-case by case basis']], label='Judging by its recent decisions, do you think the Israeli Supreme Court is generally to the left, generally to the right, or is it making decisions more on a case-by-case basis?', widget=widgets.RadioSelect)



    time_frame_past = models.IntegerField()
    time_frame_future = models.IntegerField()
    specific_decision = models.StringField()
    influence_type=models.StringField()

    def from_date(self):
        #print(dir(self))
        return 2023 - self.time_frame_past

    def to_date(self):
        return 2023 - self.time_frame_future


    def future_influence_society_choices(self):

        choice_future_list =self.choice_future_list
        print('====check choices')
        if self.influence_type == 'H':
            print('change order')

            return self.reverse_choices(choice_future_list)
        else:
            return choice_future_list



    def future_like_you_choices(self):

        choice_future_list =self.choice_future_list
        if self.influence_type == 'H':
            print('change order')

            return self.reverse_choices(choice_future_list)
        else:
            return choice_future_list


    @staticmethod
    def reverse_choices(l):
        return [str(len(l) - int(i[0]) + 1) + i[1:] for i in reversed(l)]