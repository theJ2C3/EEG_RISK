import random

from otree.api import *
from random import choice

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_QSR_guide'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    win_payoff = cu(10)
    import csv
    with open('table.csv', 'r') as para:
        para = list(csv.DictReader(para))
        row = len(para)  # number of row

    with open('outcome.csv', 'r') as draw:
        draw = list(csv.DictReader(draw))
        total = len(draw)  # number of row

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_random = models.BooleanField(initial=False)
    temp_payoff = models.CurrencyField(initial=cu(0))
    switching_point = models.IntegerField()
    red_payoff = models.CurrencyField(initial=cu(0))
    blue_payoff = models.CurrencyField(initial=cu(0))
    num_draw = models.IntegerField(initial=3)
    trial_draw = models.IntegerField(initial=1)
    outcome1 = models.IntegerField(initial=1)
    outcome2 = models.IntegerField(initial=1)
    outcome3 = models.IntegerField(initial=1)
    is_red = models.IntegerField(initial=1)
    is_red_str = models.StringField()

# PAGES
class Instruction(Page):
    pass

class Instruction2(Page):
    pass

class Instruction3(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        player.trial_draw = random.randint(1,100000)
        trial_draw = player.trial_draw
        round_row_draw = C.draw[trial_draw]
        print(round_row_draw)
        player.outcome1 = int(round_row_draw['outcome1'])
        player.outcome2 = int(round_row_draw['outcome2'])
        player.outcome3 = int(round_row_draw['outcome3'])
        player.num_draw = int(round_row_draw['numofdraw'])
        player.is_red = int(round_row_draw['jar'])


class PracticeStart(Page):
    pass

class Draw(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        b = [player.outcome1,player.outcome2,player.outcome3]

        img_paths = ['risk/{}.png'.format(i) for i in b]
        return dict(img_paths=img_paths)


class Instruction_QSR(Page):
    pass
class Instruction_QSR2(Page):
    pass
class Instruction_QSR3(Page):
    pass
class Instruction_QSR4(Page):
    pass
class QSR(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=range(1, 9, 1))

    @staticmethod
    def before_next_page(player, timeout_happened):
        # payoff calculation
        a = int(player.switching_point/10)
        round_row = C.para[a]
        print(round_row)
        player.red_payoff = int(round_row['red'])
        player.blue_payoff = int(round_row['blue'])

        if player.is_red == 0:
            player.is_red_str = "紅罐"
            player.temp_payoff = player.red_payoff
        else:
            player.is_red_str = "藍罐"
            player.temp_payoff = player.blue_payoff

class Results(Page):
    pass


page_sequence = [Instruction, Instruction2, Instruction3,Instruction_QSR,Instruction_QSR2,Instruction_QSR3,Instruction_QSR4, PracticeStart, Draw, QSR, Results]
