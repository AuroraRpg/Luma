import os
import requests
import json
gamespot = os.environ['GAMESPOT_TOKEN']


async def fetch():
  url = f"http://www.gamespot.com/api/articles/?api_key={gamespot}&format=json"
  data = requests.get(url=url)
  parsed = data.json()
  print(data)
  print(json.dumps(parsed, sort_keys=True, indent=4))
