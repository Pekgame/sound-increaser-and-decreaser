print("Loadning...")
import os
try:
    import keyboard
except:
    os.system("pip install keyboard")
    import keyboard

from hashlib import md5
from time import localtime

def clear():
    os.system("cls")

try:
    from pydub import AudioSegment
    import keyboard
except:
    clear()
    install = input("Error!\nDid you want to install the missing package?(y/n):\n")

    if install.lower() == "y":
        os.system("pip3 install pydub")
        clear()
        try:
            from pydub import AudioSegment
            import keyboard
        except:
            clear()
            print("Still Error!\n\nPackage needed:\npydub\n\nPlease install it by yourself!\n\nUsing this command!\n\n'pip install pydub'\n")
            print("Press Enter to Exit!")
            while True:
                if keyboard.is_pressed("enter"):
                    exit(0)
    elif install.lower() == "n":
        clear()
        print("Installation Cancled!\nPress Enter to Exit!")
        while True:
            if keyboard.is_pressed("enter"):
                exit(0)

clear()
filename = input("What is your file name(Ex. song.mp3):\n")
clear()
input_location = input("What is your file location(Ex. C:/Users/win10/Music):\n")+"/"+filename
clear()
random = md5(str(localtime()).encode('utf-8')).hexdigest()
output_location = input("What is ouput file location(Ex. C:/Users/win10/Music):\n")+"/"+filename.replace(".mp3", f" (Converted)_{random}.mp3")

input_sound = AudioSegment.from_mp3(input_location)
clear()

todo = int(input("What do you want to do?\n[1] Increase Volume\n[2] Decrease Volume\nChoice:\n"))

if todo == 1:
    clear()
    howmany = int(input("How many dB to Increase:\n"))
    output_sound = input_sound + howmany
    clear()
    output_sound.export(output_location, format='mp3')
    print("Press enter to exit!")
    while True:
        if keyboard.is_pressed("enter"):
            os.startfile(output_location)
            exit(0)
elif todo == 2:
    clear()
    howmany = int(input("How many dB to Decrease:\n"))
    output_sound = input_sound - howmany
    clear()
    output_sound.export(output_location, format='mp3')
    print("Press enter to exit!")
    while True:
        if keyboard.is_pressed("enter"):
            os.startfile(output_location)
            exit(0)
else:
    print("Error! Invalid input!\nPress Enter to exit!")
    while True:
        if keyboard.is_pressed("enter"):
            exit(0)
