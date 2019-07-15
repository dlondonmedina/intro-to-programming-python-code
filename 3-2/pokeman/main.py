
import requests, json

data = requests.get("https://pokeapi.co/api/v2/pokemon")
dict = json.loads(data.content)

results = dict["results"]
for result in results:
  print(result["name"])

