import os
import time


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pause(seconds):
    time.sleep(seconds)

def loader(message="Serving ice cream"):
    frames = [".  ", ".. ", "..."]

    print(message, end="", flush=True)

    for i in range(6):
        print("\r" + message + frames[i % 3], end="", flush=True)
        p(0.4)

    print()

def spinner():
    frames = ["|", "/", "-", "\\"]

    for i in range(12):
        print("\rProcessing " + frames[i % 4], end="", flush=True)
        p(0.2)

    print()  
    
cs = clear_screen
p = pause
l = loader
s = spinner