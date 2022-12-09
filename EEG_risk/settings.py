from os import environ

# roundnumfixed = 42
roundnumfixed = 3

SESSION_CONFIGS = [
    dict(
        name='risk_LC_guide',
        display_name="risk_LC_guide",
        app_sequence=['risk_LC_guide'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_BDM_guide',
        display_name="risk_BDM_guide",
        app_sequence=['risk_BDM_guide'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_QSR_guide',
        display_name="risk_QSR_guide",
        app_sequence=['risk_QSR_guide'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_LC_main_game',
        display_name="risk_LC_main_game",
        app_sequence=['risk_LC_main_game'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_BDM_main_game',
        display_name="risk_BDM_main_game",
        app_sequence=['risk_BDM_main_game'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_QSR_main_game',
        display_name="risk_QSR_main_game",
        app_sequence=['risk_QSR_main_game'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_LC_whole_game',
        display_name="risk_LC_whole_game",
        app_sequence=['risk_LC_guide', 'risk_LC_main_game', 'payment_info'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_BDM_whole_game',
        display_name="risk_BDM_whole_game",
        app_sequence=['risk_BDM_guide', 'risk_BDM_main_game', 'payment_info'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
    dict(
        name='risk_QSR_whole_game',
        display_name="risk_QSR_whole_game",
        app_sequence=['risk_QSR_guide', 'risk_QSR_main_game', 'payment_info'],
        num_demo_participants=3,
        num_of_round = roundnumfixed,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['selected_round', 'final_payoff']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'NTD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]
POINTS_CUSTOM_NAME = '法幣'
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '4595855886203'

INSTALLED_APPS = ['otree']
