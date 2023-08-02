#Tic Tac Toe
turn = "X"

def announceWinners(winner):
    print(" ")
    print(winner + " Wins!")

player1 = input("Welcome to Tic-Tac-Toe! Who is player 1(X)? ")
player2 = input("Who is player 2(O)? ")

firstSquare = "   |"
secondSquare = "   |"
thirdSquare = "   "
fourthSquare = "   |"
fifthSquare = "   |"
sixthSquare = "   "
seventhSquare = "   |"
eighthSquare = "   |"
ninthSquare = "   "

while True:
    print(firstSquare + secondSquare + thirdSquare)
    print("-----------")
    print(fourthSquare + fifthSquare + sixthSquare)
    print("-----------")
    print(seventhSquare + eighthSquare + ninthSquare)
    print(" ")
    if turn == "X":
        row = int(input(player1 + ", Enter a column(0, 1, or 2): "))
        column = int(input(player1 + ", Enter a row(0, 1, or 2): "))
        if row == 0:
            if column == 0:
                if firstSquare == "   |":
                    firstSquare = " X |"
            elif column == 1:
                if secondSquare == "   |":
                    secondSquare = " X |"
            elif column == 2:
                if thirdSquare == "   ":
                    thirdSquare = " X "
            else:
                print("haha L you wasted your turn")

        elif row == 1:
            if column == 0:
                if fourthSquare == "   |":
                    fourthSquare = " X |"
            elif column == 1:
                if fifthSquare == "   |":
                    fifthSquare = " X |"
            elif column == 2:
                if sixthSquare == "   ":
                    sixthSquare = " X "
            else:
                print("haha L you wasted your turn")

        elif row == 2:
            if column == 0:
                if seventhSquare == "   |":
                    seventhSquare = " X |"
            elif column == 1:
                if eighthSquare == "   |":
                    eighthSquare = " X |"
            elif column == 2:
                if ninthSquare == "   ":
                    ninthSquare = " X "
            else:
                print("haha L you wasted your turn")

        else:
            print("haha L you wasted your turn")

        turn = "O"


    else:
        row = int(input(player2 + ", Enter a row(0, 1, or 2): "))
        column = int(input(player2 + ", Enter a column(0, 1, or 2): "))

        if row == 0:
            if column == 0:
                if firstSquare == "   |":
                    firstSquare = " O |"
            elif column == 1:
                if secondSquare == "   |":
                    secondSquare = " O |"
            elif column == 2:
                if thirdSquare == "   ":
                    thirdSquare = " O "
            else:
                print("haha L you wasted your turn")

        elif row == 1:
            if column == 0:
                if fourthSquare == "   |":
                    fourthSquare = " O |"
            elif column == 1:
                if fifthSquare == "   |":
                    fifthSquare = " O |"
            elif column == 2:
                if sixthSquare == "   ":
                    sixthSquare = " O "
            else:
                print("haha L you wasted your turn")

        elif row == 2:
            if column == 0:
                if seventhSquare == "   |":
                    seventhSquare = " O |"
            elif column == 1:
                if eighthSquare == "   |":
                    eighthSquare = " O |"
            elif column == 2:
                if ninthSquare == "   ":
                    ninthSquare = " O "
            else:
                print("haha L you wasted your turn")

        else:
            print("haha L you wasted your turn")

        turn = "X"
    #checking for winners
    if (firstSquare == " X |" and secondSquare == " X |" and thirdSquare == " X ") or (fifthSquare == " X |" and sixthSquare == " X " and fourthSquare == " X ") or (eighthSquare == " X |" and ninthSquare == " X " and seventhSquare == " X |") or (firstSquare == " X |" and fourthSquare == " X |" and seventhSquare == " X |") or (secondSquare == " X |" and fifthSquare == " X |" and eighthSquare == " X |") or (thirdSquare == " X " and sixthSquare == " X " and ninthSquare == " X ") or (firstSquare == " X |" and fifthSquare == " X |" and ninthSquare == " X ") or (thirdSquare == " X " and fifthSquare == " X |" and seventhSquare == " X |"):
        announceWinners(player1)
        break

    # checking for O
    elif (firstSquare == " O |" and secondSquare == " O |" and thirdSquare == " O ") or (fifthSquare == " O |" and sixthSquare == " O " and fourthSquare == " O |") or (eighthSquare == " O |" and ninthSquare == " O " and seventhSquare == " O |") or (firstSquare == " O |" and fourthSquare == " O |" and seventhSquare == " O |") or (secondSquare == " O |" and fifthSquare == " O |" and eighthSquare == " O |") or (thirdSquare == " O " and sixthSquare == " O " and ninthSquare == " O ") or (firstSquare == " O |" and fifthSquare == " O |" and ninthSquare == " O ") or (thirdSquare == " O " and fifthSquare == " O |" and seventhSquare == " O |"):
        announceWinners(player2)
        break

    #checking for tie
    elif firstSquare != "   |" and secondSquare != "   |" and thirdSquare != "   " and fourthSquare != "   |" and fifthSquare != "   |" and sixthSquare != "   " and seventhSquare != "   |" and eighthSquare != "   |" and ninthSquare != "   ":
        print(" ")
        print("It's a tie!")
        break