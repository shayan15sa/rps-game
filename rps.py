import emoji
import random
import sys
import time
from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")


def animate():
    sys.stdout.write("\r    1")
    time.sleep(1)
    sys.stdout.write("\r    2")
    time.sleep(1)
    sys.stdout.write("\r    3")
    time.sleep(1)


def again():
    if input("play again ? [y/n]") == "n":
        exit()


i = True
while i:
    clear()
    print("Hi Let's play \n" + "paper or scissor or rock")
    inp = input()

    # p as paper
    # s as scissor
    # r as rock

    list = ["p", "r", "s"]
    ans = random.choice(list)

    clear()

    animate()

    clear()
    if inp == "p":
        print("you : " + emoji.emojize(":memo:"))
    elif inp == "s":
        print("you : " + emoji.emojize(":scissors:"))
    elif inp == "r":
        print("you : " + emoji.emojize(":mountain:"))

    if ans == "p":
        print("pc :" + emoji.emojize(":memo:"))
    elif ans == "s":
        print("pc :" + emoji.emojize(":scissors:"))
    elif ans == "r":
        print("pc :" + emoji.emojize(":mountain:"))

    if inp == ans:
        print("Draw!!")
        again()
        continue
    if inp == "p" and ans == "r":
        print("WIN!!")
        again()
        continue
    if inp == "r" and ans == "s":
        print("WIN!!")
        again()
        continue
    if inp == "s" and ans == "p":
        print("WIN!!")
        again()
        continue
    print("LOSE!!")
    again()
    continue
