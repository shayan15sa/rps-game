import emoji
import random

print("Hi Let's play \n" + "paper or sicsor or rock")
inp = input()
if inp == "p" or inp == "r" or inp == "s":
    exit()
list = ["p", "r", "s"]
ans = random.choice(list)
