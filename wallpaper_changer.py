import requests #  built-in requests library in python to fetch dat across the web
import random
import json
import ctypes 
import os

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02

myHeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

def set_wallpaper():
    try:
        textData = requests.get('https://www.reddit.com/r/wallpaper/new.json', headers=myHeader).content
        # print(textData)
        jsonData = json.loads(textData)

        posts = jsonData["data"]["children"]

        n = random.randint(0,len(posts)-1)
        image_url = posts[n]["data"]["url"]

        imageContents = requests.get(posts[n]["data"]["url"], headers=myHeader).content

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "wallpaper.jpg")

        with open (image_path, "wb") as imageFile:
            imageFile.write(imageContents)

        result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        if result:
            print(f"Success! Wallpaper changed to: {image_url}")
        else:
            print("Failed to set wallpaper via Windows API.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    set_wallpaper()

