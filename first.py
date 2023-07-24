feeling1 = "tired"
print("I'm " + feeling1)
# in this example, feeling1 is a variable. Note that you do not have to define the data type when you define the variable.
# also note, you do not need semicolons. DON'T FORGET IT.

print("<insert good content here>")

myAge = 13
#print("I am " + myAge + " years old")
# This would produce an error, the system cannot print two value types in the same statement, you need to convert it
myActualAge = "13"
print("I am " + myActualAge + " years old")
#This works because the system stores myActualAge as a string due to the quotation marks. Print statements will only print strings.

feeling1 = "still tired lol"
print("I'm " + feeling1)
#This will print "I'm feeling still tired lol", you can reassign variables to different values and change them

num1 = 69
num2 = 42
# Basic operators
addition = num1 + num2
print(addition)

subtraction = num1 - num2
print(subtraction)

multiplication = num1 * num2
print(multiplication)

division = num1 / num2
print(division)
# Note that unlike previously, this works because only one data type at a time is inserted in the print statement.
# Double and int aren't a thing here, you just have numbers I guess.

print(multiplication + division)
# This will not print out both numbers, it will just add the two numbers and print that. This might cause... inconviences.