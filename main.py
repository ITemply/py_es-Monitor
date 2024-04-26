import requests

esPlace = 2262441883

def getJobs(placeId):
  newRequest = requests.request('GET', f'https://games.roblox.com/v1/games/{str(placeId)}/servers/0?sortOrder=2&excludeFullGames=false&limit=100')
  return newRequest

def scanImage(pathTo):
  #change