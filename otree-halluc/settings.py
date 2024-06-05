from os import environ

SESSION_CONFIGS =   [dict(name='kt_prospective_html', num_demo_participants=4, gpt_cache=False,BotType='html',
                        app_sequence=['kt_prospective', 'thanks'],
                         profile_file ='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/kt_propect/data/modified_exclusions/pt_replication_modified_exclusions_data_shuffled.csv'),
                   dict(name='kt_prospective_dialogue', num_demo_participants=4, gpt_cache=False, BotType='dialog',
                        app_sequence=['kt_prospective', 'thanks'],
                        profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/kt_propect/data/modified_exclusions/pt_replication_modified_exclusions_data_shuffled.csv'),
                   dict(name='kt_prospective_temp0', num_demo_participants=4, gpt_cache=False,
                        app_sequence=['kt_prospective','us_profile', 'thanks'],default_engine_param={'temperature':0},
                        profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/kt_propect/data/modified_exclusions/pt_replication_modified_exclusions_data_shuffled.csv'),
                   dict (name='kt_prospective_no_profile', num_demo_participants=4, gpt_cache=False,
                        app_sequence=['kt_prospective', 'thanks'],use_profile=False),
                   dict(name='kt_prospectiveGPT', num_demo_participants=4, gpt_cache=False, use_browser_bots=True,
                        app_sequence=['kt_prospective', 'thanks']),
                 dict(name='USCourtProspective_html', num_demo_participants=20, BotType='html', gpt_cache=False,
                      profile_seq=["sex", "age",
                                   "last_elect",
                                   "educ",
                                   "religion", 'residence', 'ownhome'],
                        profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv',
                      app_sequence=['us_profile', 'survey_us_supreme_prospective', 'us_reform', 'thanks']),,
                 dict(name='USCourtProspective_dialog', num_demo_participants=20, BotType='dialog', gpt_cache=False,
                      profile_seq=["sex", "age",
                                   "last_elect",
                                   "educ",
                                   "religion", 'residence', 'ownhome'],
                        profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv',
                      app_sequence=['us_profile', 'survey_us_supreme_prospective', 'us_reform', 'thanks']),
                 dict(name='USCourtProspective_html_temp0', num_demo_participants=20, BotType='html',
                      profile_seq=["sex", "age",
                                   "last_elect",
                                   "educ",
                                   "religion", 'residence', 'ownhome'],
                      gpt_cache=False,
                      app_sequence=['us_profile', 'survey_us_supreme_prospective', 'us_reform', 'thanks'],
                      profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv',
                      default_engine_param={'temperature': 0}),
                 dict(name='USCourtProspective_dialog_temp0', num_demo_participants=20, BotType='dialog',
                      gpt_cache=False,
                      app_sequence=['us_profile', 'survey_us_supreme_prospective', 'us_reform', 'thanks'],
                      default_engine_param={'temperature': 0},
                        profile_seq=["sex", "age",
                                        "last_elect",
                                        "educ",
                                        "religion"  ,'residence','ownhome'],
                      profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv'),
                dict(name='USCourtProspective_dialog_temp0_5p', num_demo_participants=20, BotType='dialog',
                      gpt_cache=False,
                      app_sequence=['us_profile', 'survey_us_supreme_prospective', 'us_reform', 'thanks'],
                      default_engine_param={'temperature': 0},
                        profile_seq=["sex", "age",
                                        "last_elect",
                                        "educ",
                                        "religion"],
                      profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv'),
                dict(name='USCourtProspective_dialog_temp0_np', num_demo_participants=20, BotType='dialog',
                     profile_seq=["sex", "age",
                                  "last_elect",
                                  "educ",
                                  "religion", 'residence', 'ownhome'],
                      gpt_cache=False,
                      app_sequence=[ 'survey_us_supreme_prospective', 'us_reform', 'thanks'],
                      default_engine_param={'temperature': 0},
                      profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv'),
                dict(name='USCourtProspective_dialog_np', num_demo_participants=20, BotType='dialog', gpt_cache=False,
                     profile_seq=["sex", "age",
                                  "last_elect",
                                  "educ",
                                  "religion", 'residence', 'ownhome'],
                          profile_file='/Users/olivierkamoun/PycharmProjects/tau_thesis_tools/us_court_survey/full_survey_label_shuffled.csv',
                          app_sequence=[ 'survey_us_supreme_prospective', 'us_reform', 'thanks']),

                     ]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4369693803987'
