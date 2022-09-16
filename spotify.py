from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser as web
import pyautogui
from time import sleep

client_id="de74cc1a3aab49abb09123cd63d0e177"
client_secret="f30aac8fcd984ce6b1ac4519a24f5f92"
author = 'the fabulous thunderbirds'
song = "scratch my back".upper()
flag= 0

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id,client_secret))
result = sp.search(author)
for i in range(0,len(result["tracks"]["items"])):
    nameSong = result["tracks"]["items"][i]["name"].upper()
    # print(nameSong)
    if song in nameSong:
        print("Cancion Encontrada")
        flag = 1
        print(result["tracks"]["items"][i]["uri"])
        web.open(result["tracks"]["items"][i]["external_urls"]["spotify"])
        sleep(7)
        for i in range(32):
            pyautogui.press("tab")
        pyautogui.press("enter")
if flag ==0:
    web.open(f"spotify:search:{song}")
# print(result)