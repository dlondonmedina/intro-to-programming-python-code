
import requests, json

data = requests.get("https://data.nba.net/")
dict = json.loads(data.content)
team_data = dict["sports_content"]["teams"]["team"]
# print (team_data)
for team in team_data:
  if (team["is_nba_team"]):
    print(team["team_abbrev"],team["team_nickname"], team["conference"], team["division_id"])
 

