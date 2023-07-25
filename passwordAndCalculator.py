hacked = False
usernameEntered = False
guesses = 3
operation = "0"
username = "username"
password = "hi"

while hacked == False:
	if operation == "quit":
		break
	theirUsername = input("Please enter a username: ")
	theirGuess = input("Please enter a password: ")
	if theirUsername != username:
		print("Invalid Username. Please try again.")
	else:
		if password != theirGuess:
			print("no")
			guesses -=1
			print("You have:")
			print(guesses)
			print("guesses left. Don't mistype lol")
		else:
			print("Access Granted!")
			hacked = True
		
		# Starting calculator thingy
		if hacked == True:
			print("Welcome to the calculator! Why did you come here, of all places?")
			print("...")
			print("ok fine I can be a calculator")
			while True:
				# You have to capitalize booleans that's gonna be so annoying
				print(" ")
				num1 = int(input("Enter the first number: "))
				print(" ")
				operation = input("+, -, *, /, or ^(exponents)? (Enter quit to quit) ")
				print(" ")
				if operation == "quit":
					break
				num2 = int(input("Enter the second number: "))
				print(" ")
				# must type in the data type before the input, default is string
			
				if operation == "+":
					print (num1 + num2)
					if num1 + num2 == 69:
						print("nice")
			
				elif operation == "-":
					print (num1 - num2)
					if num1 - num2 == 69:
						print("nice")
				
				elif operation == "*":
					print (num1 * num2)
					if num1 * num2 == 69:
						print("nice")
				
				elif operation == "/":
					if num2 != 0:
						print (num1 / num2)
						if num1 / num2 == 69:
							print("nice")
					else:
						print ("stop trolling idot")
			
				elif operation == "^":
					print (num1**num2)
					if num1 ** num2 == 69:
						print("nice")
				else:
					print("no")
			
			
			print("ok bye")
			

# end of loop
	
if hacked == False:
	print("you guessed wrong too many times you lose LLLLLL")