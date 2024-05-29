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

author = 'Olivier Kamoun'

doc = """
Kahneman and Tversky's 1979 article on Prospect Theory i
"""


class C(BaseConstants):
    NAME_IN_URL = 'kt_prospective'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    def creating_session(self):
        import random
        n_item =17 
        for player in self.get_players():
                l = list(range(1, n_item+1))
                random.shuffle(l)
                player.item_seq  = str(l)




class Group(BaseGroup):
    pass



class Player(BasePlayer):

    item_1 =	models.StringField(	choices=[[1,'A 33% chance at 2500, a 66% chance at 2400, and a 1% chance of 0'],[2,'Guaranteed 240000 ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_2 =	models.StringField(	choices=[[1,'A 33% chance of 2500 (67% chance of 0)'],[2,'A 34% chance of 2400 (66% chance of 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_3 =	models.StringField(	choices=[[1,'An 80% chance of 4000 (20% chance of 0)'],[2,'100% guarantee of 3000 ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_4 =	models.StringField(	choices=[[1,'A 20% chance of 4000 (80% chance of 0)'],[2,'25% chance of 3000 (75% chance of 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_5 =	models.StringField(	choices=[[1,'A 45% chance of 6000 (55% chance of 0)'],[2,'90% chance of 3000 (10% chance of 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_6 =	models.StringField(	choices=[[1,'A 0.1% chance of 6000 (99.9% chance of 0)'],[2,'0.2% chance of 3000 (99.8% chance of 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_7 =	models.StringField(	choices=[[1,'An 80% chance of losing 4000 (20% chance of losing 0)'],[2,'A 100% guarantee of losing 3000 ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_8 =	models.StringField(	choices=[[1,'A 20% chance of losing 4000 (80% chance of losing 0)'],[2,'A 25% chance of losing 3000 (75% chance of losing 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_9 =	models.StringField(	choices=[[1,'A 45% chance of losing 6000 (55% chance of losing 0)'],[2,'A 90% chance of losing 3000 (10% chance of losing 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_10 =	models.StringField(	choices=[[1,'A 0.1% chance of losing 6000 (A 99.9% chance of losing 0)'],[2,'A 0.2% chance of losing 3000 (A 99.8% chance of losing 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_11 =	models.StringField(	choices=[[1,'An 80% chance of 4000 (20% chance of 0)'],[2,'A 100% guarantee of 3000 ']]	,label='Imagine you are playing a game with two levels, but you have to make a choice about the second level before you know the outcome of the first. At the first level, there is a 75% chance that the game will end without you winning anything, and a 25% chance that you will advance to the second level. What would you choose in the second level? ',widget=widgets.RadioSelect)
    item_12 =	models.StringField(	choices=[[1,'A 50% chance to gain an additional 1000 (50% chance of gaining 0 beyond what you already have)'],[2,'A 100% guarantee of gaining an additional 500 ']]	,label='Imagine we gave you 1000 right now to play a game. Which option would you prefer? ',widget=widgets.RadioSelect)
    item_13 =	models.StringField(	choices=[[1,'A 50% chance you will lose 1000 (50% chance of losing 0)'],[2,'A 100% chance you will lose 500 ']]	,label='Imagine we gave you 2000 right now to play a game. Which option would you prefer? ',widget=widgets.RadioSelect)
    item_14 =	models.StringField(	choices=[[1,'A 25% chance of 6000 (75% chance of 0)'],[2,'A 25% chance of 4000 (25% chance of 2000, 50% chance of 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_15 =	models.StringField(	choices=[[1,'A 25% chance of losing 6000 (75% chance of losing nothing)'],[2,'A 25% chance of losing 4000 (25% chance of 2000, 50% chance of 0) ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_16 =	models.StringField(	choices=[[1,'A 0.1% chance at 5000 (99.9% chance of 0)'],[2,'A 100% guarantee of 5 ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_17 =	models.StringField(	choices=[[1,'A 0.1% chance of losing 5000 (99.9% chance of losing nothing)'],[2,'A 100% guarantee of losing 5 ']]	,label='Which option do you prefer? ',widget=widgets.RadioSelect)
    item_seq = models.StringField(initial='[1]')
    item_20 =	models.StringField(	choices=[[1,'A 99% chance at  10,000 (1% change of 0)'],[2,'A 100% guarantee of losing 5,000 ']],blank=True,label='Do not answer this question  ',widget=widgets.RadioSelect)
    item_21 = models.StringField(
        choices=[[1, 'A 99% chance at  10,000 (1% change of 0)'], [2, 'A 100% guarantee of losing 5,000 ']], label='Which option do you prefer? ',
        widget=widgets.RadioSelect)





