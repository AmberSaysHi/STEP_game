import random
name = input("What is your name? ")
n = random.randint(1, 100)

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    # checking if they are trolling
    if guess > 100:
        print("bruh you idot that isn't between 1 and 100")
    elif guess < 1:
       print("bruh you idot that isn't between 1 and 100")
    else:
        # Checking the value
        if n > guess:
            print("Too small")
        elif n < guess:
         print("Too large")
        elif n == guess:
            print("wowwwwwww " + name + " has hacks report")
            playAgain = input("Enter 1 to play again, anything else to quit ")
            if playAgain != "1":
                break
            else:
                n = random.randint(1, 100)
print("ok bye")