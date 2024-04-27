import requests
import cv2
import easyocr
import os 
import webbrowser

from dotenv import load_dotenv
load_dotenv()

esPlace = os.environ['PLACE_ID']
print(esPlace)

def getJobs(placeId):
  newRequest = requests.request('GET', f'https://games.roblox.com/v1/games/{str(placeId)}/servers/0?sortOrder=2&excludeFullGames=false&limit=100')
  return newRequest

def scanImage(pathTo):
  img = cv2.imread(pathTo)
  reader = easyocr.Reader(['en'], gpu=False)
  text = reader.readtext(img)
  return text

def createJoinCode(placeId, jobId):
  formattedString = f'roblox://experiences/start?placeId={placeId}&gameInstanceId={jobId}'
  return formattedString