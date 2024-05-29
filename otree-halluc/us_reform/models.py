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

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'us_reform'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass

def double_list(l):
    return [[i,i] for i in l ]
choices_list={'court_decision':['1-Generally to the left','2-Generally to the right','3-Case by case basis' ],
                  'political_ide':['1-Very left wing', '2-Left of center','3-neutral', '4-Right of center',
                                   '5-Very right wing','99-Don’t know'],
                  'political_aff': ['1-Voted for a party not in the coalition','2-Voted for a party in the coalition',
                                    '3-Didn''t vote','4-Not a voter'],
                  'political_gov_sup':['1-Strongly Oppose', '2-Somewhat Oppose',
                                       '3-Neutral (Neither Oppose or Support)', '4-Somewhat Support', '5-Strongly Support '],
                  'status':['1-Foreign', '2-New Immigrant', '3-Israeli born'],
                  'sex':['1-Male', '2-Female', '3-Other'],
                  'educ':['1-Did not finish high school', '2-High school graduate', '3-Some college', '4-College graduate',
                   '5-Post graduate degree'],
                  'court_knowledge':['1-Very knowledgeable', '2-Somewhat knowledgeable', '3-Average knowledge',
                   '4-Not very knowledgeable', '5-I don’t know anything about the Court '],
                  'court_interest':['1-Not at all interested', '2-Somewhat interested', '3-Very interested'],
                  'court_interst_since':['1-I’ve always been interested in the Court', '2-My interest in the Court is more recent',
                   '3-I am not interested in the court'],
                   'religion':['1-Religious jew','2-Secular jew','3-Religious muslim','4-Secular muslim',
                                     '5-Religious christian','6-Secular christian',
                                     '7-Atheist','99-Other' ] ,
                    'next_election':['1-Current coalition ','2-Opposition','3-other']}
choice_support_list = ['1-strongly support',  '2-somewhat support',
                       '3-slightly support',  '4-slightly oppose',
                       '5-somewhat oppose','6-strongly oppose']
class Player(BasePlayer):
    changes = models.StringField(choices=choice_support_list , label='Do you support or oppose making changes to the Supreme Court.', widget=widgets.RadioSelect)
    court_knowledge = models.StringField(choices=double_list(choices_list['court_knowledge']), label='In general, how knowledgeable would you say you are about the Supreme Court compared to other citizens in Israel?', widget=widgets.RadioSelect)
    court_interest = models.StringField(choices=double_list(choices_list['court_interest']), label='How interested are you in the Israeli Supreme Court', widget=widgets.RadioSelect)
    court_interst_since = models.StringField(choices=double_list(choices_list['court_interst_since']), label='Some people have always been interested in the Israeli Supreme Court, others have just recently become interested in that institution in light of current events.  Would you say that your interest in the Court is longstanding or more recent.', widget=widgets.RadioSelect)
    next_election = models.StringField(choices=double_list(choices_list['next_election']), label='Who do you think will win next election?', widget=widgets.RadioSelect)
    #change_override = models.StringField(choices=choice_support_list, label='Override clause based on regular majority of 61 MKs.', widget=widgets.RadioSelect)
    change_term = models.StringField(choices=choice_support_list, label='Changing the lifetime term of membership on the Supreme Court to a period of 18 years.', widget=widgets.RadioSelect)

    change_selection = models.StringField(choices=choice_support_list, label='Electing Supreme Court justices rather than having them appointed by the President.', widget=widgets.RadioSelect)
    #change_reasonable = models.StringField(choices=choice_support_list, label='limiting the use of the Reasonableness.', widget=widgets.RadioSelect)
    change_size = models.StringField(choices=choice_support_list,
                                          label='Adding several justices to the Supreme Court above its current level of 9.',
                                          widget=widgets.RadioSelect)

    court_decision = models.StringField(choices=[['1-generally to the left ', '1-generally to the left'], ['2-generally to the right', '2-generally to the right'], ['3-case by case basis', '3-case by case basis']], label='Judging by its recent decisions, do you think the Israeli Supreme Court is generally to the left, generally to the right, or is it making decisions more on a case-by-case basis?', widget=widgets.RadioSelect)
    pages_excluded = models.StringField()
def my_function(player: Player):
    pass
