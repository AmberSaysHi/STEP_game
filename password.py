# alright password time

hacked = False
guesses = 3
password = input("What do you want your password to be? ")
while guesses > 0:
	theirGuess = input("Please enter a password: ")
	
	if theirGuess == password:
		print("Access Granted!")
		hacked = True
		break
	
	else:
		print("no")
		guesses -=1
		print("you have")
		print(guesses)
		print("guesses left. Don't mistype lol")
# end of loop
	
if hacked == False:
	print("you guessed wrong too many times you lose LLLLLL")
	
# that took way less time than I thought it would I am very bored now