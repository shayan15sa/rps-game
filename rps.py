import emoji
import random
import sys
import time

print("Hi Let's play \n" + "paper or scissor or rock")
inp = input()
if inp == "p" or inp == "r" or inp == "s":
    exit()
list = ["p", "r", "s"]
ans = random.choice(list)


def animate():
    sys.stdout.write("\rloading |")
    time.sleep(0.1)
    sys.stdout.write("\rloading /")
    time.sleep(0.1)
    sys.stdout.write("\rloading -")
    time.sleep(0.1)
    sys.stdout.write("\rloading \\")
    time.sleep(0.1)
    sys.stdout.write("\rDone!     ")


if ans == "p":
    print(emoji.emojize(":memo:"))
elif ans == "s":
    print(emoji.emojize(":scissor:"))
elif ans == "r":
    print(emoji.emojize(":mountain:"))
