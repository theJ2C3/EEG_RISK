import random
from otree.api import *
from random import choice

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_LC_guide'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    win_payoff = cu(10)

    # import drawing dataset
    import csv
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
    left_side_amount = models.IntegerField(initial=100)
    switching_point = models.IntegerField()
    num_draw = models.IntegerField(initial=3)
    trial_draw = models.IntegerField(initial=1)
    outcome1 = models.IntegerField(initial=1)
    outcome2 = models.IntegerField(initial=1)
    outcome3 = models.IntegerField(initial=1)
    is_red = models.IntegerField(initial=1)
    is_red_str = models.StringField()
    row = models.IntegerField(initial=1)
    lottery = models.IntegerField(initial=1)


# PAGES
class Instruction(Page):
    pass

class Instruction2(Page):
    pass

class Instruction3(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        # draw the trial of dataset used in this round
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
        # output ball image by result above
        b = [player.outcome1,player.outcome2,player.outcome3]

        img_paths = ['risk/{}.png'.format(i) for i in b]
        return dict(img_paths=img_paths)


class Instruction_LC(Page):
    pass
class Instruction_LC2(Page):
    pass
class Instruction_LC3(Page):
    pass
class Instruction_LC4(Page):
    pass
class Instruction_LC5(Page):
    pass
class Instruction_LC6(Page):
    pass

class LC(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=range(1, 9, 1))

    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        # draw the row used for determination
        player.row = random.randint(1, 9)
        # draw random lottery number
        player.lottery = random.randint(1, 9)
        # payoff calculation
        if player.is_red == 0:
            player.is_red_str = "紅罐"
        else:
            player.is_red_str = "藍罐"

        if player.row >= player.switching_point:
            player.is_random = True
            if player.lottery >= player.row:
                player.temp_payoff = 0
            else:
                player.temp_payoff = 200
        else:
            player.is_random = False
            if player.is_red == 0:
                player.temp_payoff = 200
            else:
                player.temp_payoff = 0



class Results(Page):
    pass


page_sequence = [Instruction, Instruction2, Instruction3, Instruction_LC, Instruction_LC2, Instruction_LC3, Instruction_LC4,Instruction_LC5, Instruction_LC6, PracticeStart, Draw, LC , Results]
# page_sequence = [Instruction3, Draw, LC , Results]

