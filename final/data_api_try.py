import pandas as pd
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams

# 1) Find the Warriors' team ID
nba_teams = teams.get_teams()
gsw = next(t for t in nba_teams if t["full_name"] == "Golden State Warriors")
team_id = gsw["id"]

# 2) Fetch game logs for the 2023-24 season
response = teamgamelog.TeamGameLog(
    team_id=team_id,
    season="2023-24",
    season_type_all_star="Regular Season"
)

# 3) Extract the DataFrame correctly
df = response.get_data_frames()[0]

# 4) Convert date column and filter
df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])
target_date = pd.to_datetime("2023-12-01")
df_before = df[df["GAME_DATE"] <= target_date]

print(df_before)

# Optional: get aggregated stats up to that date
summary = df_before[["PTS","REB","AST"]].sum()
print("Totals up to 12/1/23:", summary)




