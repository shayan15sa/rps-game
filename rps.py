import emoji
import random

print("Hi Let's play \n" + "paper or scissor or rock")
inp = input()
if inp == "p" or inp == "r" or inp == "s":
    exit()
list = ["p", "r", "s"]
ans = random.choice(list)

if ans == "p":
    print(emoji.emojize(":memo:"))
elif ans == "s":
    print(emoji.emojize(":scissor:"))
elif ans == "r":
    print(emoji.emojize(":mountain:"))
