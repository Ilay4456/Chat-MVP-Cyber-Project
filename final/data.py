from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999')

# pandas data frames (optional: pip install pandas)
#career.season_totals_regular_season.get_data_frame()

# json
#career.get_json()

# dictionary
#career.get_dict()

'''df = career.season_totals_regular_season.get_data_frame()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)'''


from nba_api.stats.endpoints import teamgamelog

# fetch games for a given team up to a specific date
log = teamgamelog.TeamGameLog(
    team_id='1610612739',       # example team ID
    season='2024-25',           # NBA season format
    season_type_all_star='Regular Season',
    date_from_nullable='',
    date_to_nullable='2025-12-31'  # all games until Dec 31, 2025
)

'''df = log.get_data_frames()[0]
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)'''


from nba_api.stats.endpoints import leaguegamelog

log = leaguegamelog.LeagueGameLog(
    season="2024-25",
    season_type_all_star="Regular Season"
)
df = log.get_data_frames()[0]
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)









