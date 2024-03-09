import requests #  built-in requests library in python to fetch dat across the web
import random
import json
import ctypes 

textData = requests.get('https://www.reddit.com/r/wallpaper/new.json').content
# print(textData)
jsonData = json.loads(textData)
print(jsonData)
posts = jsonData["data"]["children"]

n = random.randint(0,len(posts)-1)

imageContents = requests.get(posts[n]["data"]["url"]).content

with open ("wallpaper.jpg", "wb") as imageFile:
    imageFile.write(imageContents)


SPI_SETDESKWALLPAPER = 20

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"%FILE_DESTIONATION_YOU_WANT_TO_STORE_THE_IMAGE%" , 3)

