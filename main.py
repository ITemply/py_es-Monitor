import requests
import cv2
import easyocr

esPlace = 2262441883

def getJobs(placeId):
  newRequest = requests.request('GET', f'https://games.roblox.com/v1/games/{str(placeId)}/servers/0?sortOrder=2&excludeFullGames=false&limit=100')
  return newRequest

def scanImage(pathTo):
  img = cv2.imread(pathTo)
  reader = easyocr.Reader(['en'], gpu=False)
  text = reader.readtext(img)
  print(text)

scanImage('images/image.png')