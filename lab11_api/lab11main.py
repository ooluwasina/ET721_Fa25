"""
Daniel Oluwasina
Lab 11
Oct 22, 2025
"""

import pandas as pd
#Example 1: Dataframe
dict_ = {'a': [11,21,31], 'b':[12,22,32]}

#create a dataframe of dict
df = pd.DataFrame(dict_)

#display the first few rows of the dataframe
print(df.head())

print(df.mean())
#Example 2: Get NBA teams
from static import get_teams

nba_teams = get_teams()
print(f"First 2 teams: {nba_teams[:2]}")

#convert list of dictionaries into dataframe
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

df_warrior = df_teams[df_teams["nickname"]== 'Warriors']
print(df_warrior)

warrior_id = df_warrior[["id"]].values[0][0]
print(f"\nwarrior id = {warrior_id}")

import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl" 

file_name = "Golden_State.pkl"

print("\nDownloading external Data")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("download complete")
else:
    print("download failed")


games = pd.read_pickle(file_name)
print("\nGames data from pickle file:")
print(games.head())

warriors_vs_raptors = games[games['MATCHUP'].str.contains("TOR")]

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains(" vs. ")]

gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains(" @ ")]

home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_home_vs_raptors['PTS'].mean()

print(f"\nWarriors home average {home_avg_plus}")
print(f"\nWarriors away average {away_avg_plus}")

import matplotlib.pyplot as plt

metrics = ["PLUS_MINUS", 'PTS']
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label = "Home", color = "skyblue")

plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label = "Away", color = "orange")

plt.xticks(x, metrics)
plt.title("Golden State Warriors vs. Raptors - Home vs Away Comparison")
plt.ylabel("Average value")
plt.legend()
plt.grid(axis='y', linestyle = "--", alpha=0.7)
plt.tight_layout()
plt.show(block = True)
input("press enter to close...")