import random

from otree.api import *
from random import choice

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_LC_main_game'
    PLAYERS_PER_GROUP = None
    # NUM_ROUNDS = 5
    NUM_ROUNDS = 63
    win_payoff = cu(10)

    # import drawing dataset
    import csv
    with open('outcome.csv', 'r') as draw:
        draw = list(csv.DictReader(draw))
        total = len(draw)


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
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Draw(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        # draw the trial of dataset used in this round
        import random
        player.trial_draw = random.randint(1,C.total)
        trial_draw = player.trial_draw
        round_row_draw = C.draw[trial_draw]
        print(round_row_draw)
        player.outcome1 = int(round_row_draw['outcome1'])
        player.outcome2 = int(round_row_draw['outcome2'])
        player.outcome3 = int(round_row_draw['outcome3'])
        player.num_draw = int(round_row_draw['numofdraw'])
        player.is_red = int(round_row_draw['jar'])

        b = [player.outcome1, player.outcome2, player.outcome3]

        # output ball image by result above

        img_paths = ['risk/{}.png'.format(i) for i in b]
        return dict(img_paths=img_paths)

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
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # draw one round as final payoff
        import random
        participant = player.participant

        # if it's the last round
        # if player.round_number == C.NUM_ROUNDS:
        #     random_round = random.randint(1, C.NUM_ROUNDS)
        if player.round_number == player.session.config["num_of_round"]:
            random_round = random.randint(1, player.session.config["num_of_round"])
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            participant.final_payoff  = player_in_selected_round.temp_payoff
            
    def app_after_this_page(player, upcoming_apps):
        # print(player.session.config["app_sequence"][2])
        # print(player.session.config["num_of_round"])
        if player.round_number == player.session.config["num_of_round"]:             
            # 假如回合數已經到達變跳到最後一頁
            return upcoming_apps[0]


page_sequence = [Instruction, Draw, LC, Results]
