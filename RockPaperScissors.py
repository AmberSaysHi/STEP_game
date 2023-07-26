import random

computer = random.randint(1,3)
player = int(input("Enter 1 for rock, 2 for paper, and 3 for scissors: "))
if player > 3 or player < 1:
    print("bro really tried to cheat I'm banning you lol")

if player == 1:
    if computer == 2:
        print("Computer chose paper")
        print("Computer wins! haha LLL")
    elif computer == 3:
        print("Computer chose scissors")
        print("wowwww hacks you won")
    else:
        print("Computer chose rock")
        print("it's a tie...")

if player == 2:
    if computer == 3:
        print("Computer chose scissors")
        print("Computer wins! haha LLL")
    elif computer == 1:
        print("Computer chose rock")
        print("wowwww hacks you won")
    else:
        print("Computer chose paper")
        print("it's a tie...")

if player == 3:
    if computer == 1:
        print("Computer chose rock")
        print("Computer wins! haha LLL")
    elif computer == 2:
        print("Computer chose paper")
        print("wowwww hacks you won")
    else:
        print("Computer chose scissors")
        print("it's a tie...")