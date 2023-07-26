num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    if num1 > num3:
        print("The first number")
        print(num1)
        print("was the greatest.")
        greatest = num1

    else:
        print("The third number")
        print(num3)
        print("was the greatest.")
        greatest = num3

else:
    if num2 > num3:
        print("The second number")
        print(num2)
        print("was the greatest.")
        greatest = num2

    else:
        print("The third number")
        print(num3)
        print("was the greatest.")
        greatest = num3

if greatest == num1:
    if num2 > num3:
        print("The second number was second, and the third number was smallest.")
    else:
        print("The third number was second, and the second number was smallest.")

elif greatest == num2:
    if num1 > num3:
        print("The first number was second, and the third number was smallest.")
    else:
        print("The first number was second, and the third number was smallest.")

else:
    if num1 > num2:
        print("The first number was second, and the second number was smallest.")
    else:
        print("The second number was second, and the first number was smallest.")