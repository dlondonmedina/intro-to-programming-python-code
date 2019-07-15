import requests, json

data = requests.get("https://catfact.ninja/breeds?limit=5")
dict = json.loads(data.content)
print(dict["data"])

for cat in dict["data"]:
  for property in cat:
    print(property,":",cat[property])
  print("------------")


