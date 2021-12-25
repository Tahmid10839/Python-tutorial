
# Healthy Programmer

# 9am-5pm
# water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 - 45 min - ExDone - log
# Rules
# pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a==stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} [{datetime.now()}]\n")


if __name__ == '__main__':
    # musiconloop("water.mp3","stop")

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 40*60
    eyessec = 30*60
    exsec = 45*60

    while True:
        if time()-init_water > watersec:
            print("Water drinking time. Enter 'drank' to stop the alarm")
            musiconloop("water.mp3","drank")
            init_water = time()
            log(f"Drank water at")
        elif time()-init_eyes > eyessec:
            print("Eye Exercise time. Enter 'eydone' to stop the alarm")
            musiconloop("eye.mp3","eydone")
            init_eyes = time()
            log(f"Eye relaxed at")
        elif time()-init_exercise > exsec:
            print("Physical activity time. Enter 'exdone' to stop the alarm")
            musiconloop("exercise.mp3","exdone")
            init_exercise = time()
            log(f"Physical exercised at")


