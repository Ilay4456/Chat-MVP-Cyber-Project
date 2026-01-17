import requests
import pandas as pd
import time
import numpy as np

BASE_URL = "https://stats.nba.com/stats/leagueLeaders"

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
    "connection": "keep-alive",
    "host": "stats.nba.com",
    "origin": "https://www.nba.com",
    "referer": "https://www.nba.com/",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

# seasons like 2012-13 ... 2024-25
seasons = [f"{y}-{str(y+1)[-2:]}" for y in range(2012, 2025)]
season_types = ["Regular Season", "Playoffs"]

all_frames = []
t0 = time.time()

for season in seasons:
    for stype in season_types:
        params = {
            "LeagueID": "00",
            "PerMode": "Totals",
            "Scope": "S",
            "Season": season,          # <-- correct format
            "SeasonType": stype,       # <-- human-readable; params handles spaces
            "StatCategory": "PTS",
        }
        resp = requests.get(BASE_URL, headers=headers, params=params, timeout=30)
        data = resp.json()

        # Handle both "resultSet" and "resultSets"
        rs = None
        if "resultSet" in data:
            rs = data["resultSet"]
        elif "resultSets" in data and data["resultSets"]:
            rs = data["resultSets"][0]
        else:
            print(f"⚠️ Unexpected response for {season}, {stype}; skipping.")
            continue

        df = pd.DataFrame(rs["rowSet"], columns=rs["headers"])
        df.insert(0, "Season", season)
        df.insert(1, "SeasonType", stype)
        all_frames.append(df)

        print(f"Finished {season}, {stype}.")
        time.sleep(np.random.uniform(5, 12))  # be polite

runtime_min = (time.time() - t0) / 60
print(f"Process completed! Total run time: {runtime_min:.2f} min")

final_df = pd.concat(all_frames, ignore_index=True) if all_frames else pd.DataFrame()
final_df.to_excel("nba_player_data.xlsx", index=False)
print("Saved to nba_player_data.xlsx")
