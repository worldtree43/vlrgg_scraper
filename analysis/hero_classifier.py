import pandas as pd

df = pd.read_csv('../data/match_result_data/bilibili-gaming-vs-kr-esports-valorant-champions-2024-elim-a.csv')

agents_roles = {
    "kayo": ["Flash Initiator","Initiator"],
    "cypher": ["Sentinel"],
    "omen": ["Controller"],
    "yoru": ["First Duelist","Second Duelist","Duelist","Initiator"],
    "deadlock": ["Sentinel"],
    "gekko": ["Flash Initiator", "Initiator"],
    "killjoy": ["Sentinel"],
    "harbor": ["Wall Controller","Controller"],
    "jett": ["Duelist"],
    "brimstone": ["Controller"],
    "fade": ["Initiator"],
    "astra": ["Controller"],
    "chamber": ["Sentinel","Duelist"],
    "sage": ["Sentinel"],
    "reyna": ["Second Duelist","Duelist"],
    "neon": ["Duelist"],
    "phoenix": ["Duelist"],
    "sova": ["Initiator"],
    "viper": ["Sentinel","Controller"],
    "skye": ["Initiator"],
    "breach": ["Initiator"],
    "iso": ["Second Duelist","Duelist"],
    "clove": ["Sentinel"],
    "raze": ["Duelist"]
}

agents_roles = {key.lower(): value for key, value in agents_roles.items()}

df['hero_name_lower'] = df['Hero Name'].str.lower()
df['role'] = df['hero_name_lower'].map(agents_roles)

grouped = df.groupby('Map')

matchups = []

for map_name, group in grouped:
    teams = group['Team Name'].unique()

    team1 = group[group['Team Name'] == teams[0]]
    team2 = group[group['Team Name'] == teams[1]]

    for _, player1 in team1.iterrows():
        match = team2[team2['hero_name_lower'] == player1['hero_name_lower']]
        if not match.empty:
            player2 = match.iloc[0]
            matchups.append((player1['Player Name'], player2['Player Name'], map_name))
            team2 = team2[team2['Player Name'] != player2['Player Name']]
    for _, player1 in team1.iterrows():
        match = team2[team2['role'] == player1['role']]
        if not match.empty:
            player2 = match.iloc[0]
            matchups.append((player1['Player Name'], player2['Player Name'], map_name))
            team2 = team2[team2['Player Name'] != player2['Player Name']]

for player1, player2, map_name in matchups:
    print(f"On map {map_name}, {player1} (Team 1) is matched with {player2} (Team 2)")