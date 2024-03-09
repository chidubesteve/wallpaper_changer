import requests #  built-in requests library in python to fetch dat across the web
import random
import json
import ctypes 

SPI_SETDESKWALLPAPER = 20
myHeader = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

textData = requests.get('https://www.reddit.com/r/wallpaper/new.json', headers=myHeader).content
# print(textData)
jsonData = json.loads(textData)

posts = jsonData["data"]["children"]

n = random.randint(0,len(posts)-1)

imageContents = requests.get(posts[n]["data"]["url"], headers=myHeader).content

with open ("wallpaper.jpg", "wb") as imageFile:
    imageFile.write(imageContents)

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"%FILE_DESTIONATION_YOU_WANT_TO_STORE_THE_IMAGE%`", 3)

