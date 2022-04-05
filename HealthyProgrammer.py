#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio
from time import time
from pygame import mixer
from datetime import datetime
def mus(file,stp):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        op=input("Enter: ")
        if op==stp:
            mixer.music.stop()
            break
def logo(mt):
    with open("logs.txt","a") as f:
        f.write(f"{mt} {datetime.now()}\n")
if __name__=='__main__':
    iwater=time()
    ieye=time()
    iex=time()
    water=40*60
    eye=30*60
    ex=45*60
    while True:
        if time()-iwater > water:
            print("Drink 1 Glass of water right now. Type 'drank' after drinking")
            mus('police.mp3','drank')
            iwater=time()
            logo("Drank water at")
        if time()-ieye > eye:
            print("Blink right now. Type 'blink' after blinking")
            mus('chinese.mp3','blink')
            ieye=time()
            logo("Blinked at")
        if time()-iex > ex:
            print("Excercise right now. Type 'excercised' after drinking")
            mus('boy.mp3','excercised')
            iex=time()
            logo("Excercised at")