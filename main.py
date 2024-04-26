import requests
import easyocr

esPlace = 2262441883

def getJobs(placeId):
  newRequest = requests.request('GET', f'https://games.roblox.com/v1/games/{str(placeId)}/servers/0?sortOrder=2&excludeFullGames=false&limit=100')
  return newRequest

def scanImage(pathTo):
  reader = easyocr.Reader(['ch_tra', 'en'])
  result = reader.readtext(pathTo)
  print(result)

scanImage('images/image.png')