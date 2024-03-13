import requests
# import sqlalchemy

resp = requests.get('https://weather.talkpython.fm/api/weather?city=mumbai&state=OR&country=in&units=metric')
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']

print(f"hello world, it's {temp} outside!")