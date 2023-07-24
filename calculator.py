# Now that we know the rules, let's try and make smth. They told me to make a calculator

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

