import requests
import pandas as pd
import time
import numpy as np
import random

test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'
r = requests.get(url=test_url).json()

#print(r['resultSet']['headers'])
#table_headers = r['resultSet']['headers'] #list of stat types
#print(r['resultSet']['rowSet'][0])



'''pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
print(pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers))'''


table_headers = r['resultSet']['headers'] #list of stat types

'''temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
temp_df2 = pd.DataFrame({'Year':['2012-2013' for i in range(len(temp_df1))], 'Season_type':['Regular%20Season' for i in range(len(temp_df1))]})

temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)'''




df_cols = ['Year', 'Season_type']+table_headers
pd.DataFrame(columns=df_cols)

df = pd.DataFrame(columns=df_cols)
season_types = ['Regular%20Season', 'Playoffs']
years = ['2012-13', '2013-14']#[]
'''for start in range(2012, 2025):
    end = start + 1
    years.append(f"{start}-{end}")'''
''', '2014-15', '2015-16', '2016-17',
 '2017-18', '2018-19', '2019-20', '2020-21', '2021-22',
 '2022-23', '2023-24', '2024-25' '''

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


begin_loop = time.time()
table_headers = r['resultSet']['headers'] #list of stat types
for y in years:
    for s in season_types:
        api_url = f"https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season="+y+"&SeasonType="+s+"&StatCategory=PTS"
        r = requests.get(url=api_url, headers=headers).json() #, headers=headers
        temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
        temp_df2 = pd.DataFrame({'Year': [y for i in range(len(temp_df1))],
                                 'Season_type': [s for j in range(len(temp_df1))]})

        temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
        df = pd.concat([df,temp_df3], axis=0)
        print(f'Finished scarping data for the {y},{s}.')
        lag = np.random.uniform(5,40)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        print(df)
        print(f"...waiting {round(lag, 1)} seconds")
        time.sleep(lag)

end_loop = time.time()
print(f"Proces completed! Total run time: {round((end_loop-begin_loop)/60, 2)}min")
#df.to_excel('nba_player_data_xlsk', index=False)

