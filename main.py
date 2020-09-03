import keyboard
from playsound import playsound

import threading
import random
import os

#new imports
import sys
import time
# Value can be changed.
# The max number of sounds allow to be played at the same time

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if(len(sys.argv) == 1 or
    sys.argv[1].lower() == "frog"):
    
    max_sounds = 10
    sounds_folder="./sounds"

    # ----------------------------------------
    # FROM HERE ON DOWN DON'T THE CHANGE CODE!
    #                (or do?)
    # ----------------------------------------

    # Loads all sounds files from "sounds" directory in the same parent directory as main program.
    files = os.listdir(sounds_folder)
    sounds_absolute_path = os.path.abspath(sounds_folder)
    files = [f'{sounds_absolute_path}/{file}' for file in files]

    sounds_playing = threading.Semaphore(max_sounds)

    def playsong():
        # Picks a random sound from the list of sound files
        random_index = random.randrange(len(files))
        random_sound = files[random_index]
        playsound(random_sound)

        # Release semaphore
        sounds_playing.release()

    while True:
        event = keyboard.read_event()

        # When key is pressed start thread for playing sound
        # and check if we can decrement semaphore counter
        if event.event_type == "down" and sounds_playing.acquire(blocking=False):
            thread = threading.Thread(target=playsong)
            thread.start()

elif(sys.argv[1].lower() == "rick roll" or
    sys.argv[1].lower() == "rick" or
    sys.argv[1].lower() == "roll"):
    
    def play():
            sounds_folder="./sounds2"
            files = os.listdir(sounds_folder)
            playlistnum = files.index("rickRoll.mp3")
            sounds_absolute_path = os.path.abspath(sounds_folder)
            files = [f'{sounds_absolute_path}/{file}' for file in files]
            playsound(files[playlistnum])
            return

    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            play()

elif(sys.argv[1].lower() == "dadamane" or
    sys.argv[1].lower() == "da" or
    sys.argv[1].lower() == "me" or
    sys.argv[1].lower() == "ne"):
    
    def play():
            sounds_folder="./sounds2"
            files = os.listdir(sounds_folder)
            playlistnum = files.index("Dadamane.mp3")
            sounds_absolute_path = os.path.abspath(sounds_folder)
            files = [f'{sounds_absolute_path}/{file}' for file in files]
            playsound(files[playlistnum])
            return
            
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            play()
            
            

