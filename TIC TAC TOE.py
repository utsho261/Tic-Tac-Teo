import random
box = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def CreateBoard():
    print("\n\n             TIC TAC TOE")
    print(f"             ___|____|___")
    print(f"              {get_colored(box[1])} | {get_colored(box[2])}  | {get_colored(box[3])}")
    print(f"             ___|____|___")
    print(f"              {get_colored(box[4])} | {get_colored(box[5])}  | {get_colored(box[6])}")
    print(f"             ___|____|___")
    print(f"              {get_colored(box[7])} | {get_colored(box[8])}  | {get_colored(box[9])}")
    print("")

def get_colored(value):
    if value == 'X':
        return f"{GREEN}{value}{RESET}"
    elif value == 'O':
        return f"{RED}{value}{RESET}"
    else:
        return value
    print("")



def comp_win():
    if box[1] == 'O' and box[2] == 'O' and box[3] == '3':
        box[3] = mark
        print(3)
        return 1

    elif box[1] == 'O' and box[3] == 'O' and box[2] == '2':
        box[2] = mark
        print(2)
        return 1

    elif box[2] == 'O' and box[3] == 'O' and box[1] == '1':
        box[1] = mark
        print(1)
        return 1

    elif box[4] == 'O' and box[5] == 'O' and box[6] == '6':
        box[6] = mark
        print(6)
        return 1

    elif box[4] == 'O' and box[6] == 'O' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[6] == 'O' and box[5] == 'O' and box[4] == '4':
        box[4] = mark
        print(4)
        return 1

    elif box[7] == 'O' and box[8] == 'O' and box[9] == '9':
        box[9] = mark
        print(9)
        return 1

    elif box[7] == 'O' and box[9] == 'O' and box[8] == '8':
        box[8] = mark
        print(8)
        return 1

    elif box[8] == 'O' and box[9] == 'O' and box[7] == '7':
        box[7] = mark
        print(7)
        return 1

    elif box[1] == 'O' and box[4] == 'O' and box[7] == '7':
        box[7] = mark
        print(7)
        return 1

    elif box[1] == 'O' and box[7] == 'O' and box[4] == '4':
        box[4] = mark
        print(4)
        return 1
    elif box[4] == 'O' and box[7] == 'O' and box[1] == '1':
        box[1] = mark
        print(1)
        return 1

    elif box[2] == 'O' and box[5] == 'O' and box[8] == '8':
        box[8] = mark
        print(8)
        return 1

    elif box[2] == 'O' and box[8] == 'O' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[5] == 'O' and box[8] == 'O' and box[2] == '2':
        box[2] = mark
        print(2)
        return 1

    elif box[3] == 'O' and box[6] == 'O' and box[9] == '9':
        box[9] = mark
        print(9)
        return 1

    elif box[3] == 'O' and box[9] == 'O' and box[6] == '6':
        box[6] = mark
        print(6)
        return 1

    elif box[6] == 'O' and box[9] == 'O' and box[3] == '3':
        box[3] = mark
        print(3)
        return 1

    elif box[1] == 'O' and box[5] == 'O' and box[9] == '9':
        box[9] = mark
        print(9)
        return 1

    elif box[1] == 'O' and box[9] == 'O' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[5] == 'O' and box[9] == 'O' and box[1] == '1':
        box[1] = mark
        print(1)
        return 1

    elif box[3] == 'O' and box[5] == 'O' and box[7] == '7':
        box[7] = mark
        print(7)
        return 1

    elif box[3] == 'O' and box[7] == 'O' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[5] == 'O' and box[7] == 'O' and box[3] == '3':
        box[3] = mark
        print(3)
        return 1

    else:
        return 0

def block_user():
    if box[1] == 'X' and box[2] == 'X' and box[3] == '3':
        box[3] = mark
        print(3)
        return 1

    elif box[1] == 'X' and box[3] == 'X' and box[2] == '2':
        box[2] = mark
        print(2)
        return 1

    elif box[2] == 'X' and box[3] == 'X' and box[1] == '1':
        box[1] = mark
        print(1)
        return 1

    elif box[4] == 'X' and box[5] == 'X' and box[6] == '6':
        box[6] = mark
        print(6)
        return 1

    elif box[4] == 'X' and box[6] == 'X' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[6] == 'X' and box[5] == 'X' and box[4] == '4':
        box[4] = mark
        print(4)
        return 1

    elif box[7] == 'X' and box[8] == 'X' and box[9] == '9':
        box[9] = mark
        print(9)
        return 1

    elif box[7] == 'X' and box[9] == 'X' and box[8] == '8':
        box[8] = mark
        print(8)
        return 1

    elif box[8] == 'X' and box[9] == 'X' and box[7] == '7':
        box[7] = mark
        print(7)
        return 1

    elif box[1] == 'X' and box[4] == 'X' and box[7] == '7':
        box[7] = mark
        print(7)
        return 1

    elif box[1] == 'X' and box[7] == 'X' and box[4] == '4':
        box[4] = mark
        print(4)
        return 1
    elif box[4] == 'X' and box[7] == 'X' and box[1] == '1':
        box[1] = mark
        print(1)
        return 1

    elif box[2] == 'X' and box[5] == 'X' and box[8] == '8':
        box[8] = mark
        print(8)
        return 1

    elif box[2] == 'X' and box[8] == 'X' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[5] == 'X' and box[8] == 'X' and box[2] == '2':
        box[2] = mark
        print(2)
        return 1

    elif box[3] == 'X' and box[6] == 'X' and box[9] == '9':
        box[9] = mark
        print(9)
        return 1

    elif box[3] == 'X' and box[9] == 'X' and box[6] == '6':
        box[6] = mark
        print(6)
        return 1

    elif box[6] == 'X' and box[9] == 'X' and box[3] == '3':
        box[3] = mark
        print(3)
        return 1

    elif box[1] == 'X' and box[5] == 'X' and box[9] == '9':
        box[9] = mark
        print(9)
        return 1

    elif box[1] == 'X' and box[9] == 'X' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[5] == 'X' and box[9] == 'X' and box[1] == '1':
        box[1] = mark
        print(1)
        return 1

    elif box[3] == 'X' and box[5] == 'X' and box[7] == '7':
        box[7] = mark
        print(7)
        return 1

    elif box[3] == 'X' and box[7] == 'X' and box[5] == '5':
        box[5] = mark
        print(5)
        return 1

    elif box[5] == 'X' and box[7] == 'X' and box[3] == '3':
        box[3] = mark
        print(3)
        return 1

    else:
        return 0

def checkWinner():
    #Horizontal matching condition...
    if box[1] == box[2] and box[2] == box[3]:
        return 1
    elif box[4] == box[5] and box[5] == box[6]:
        return 1
    elif box[7] == box[8] and box[8] == box[9]:
        return 1

    #Vartical matching condition...
    elif box[1] == box[4] and box[4] == box[7]:
        return 1
    elif box[2] == box[5] and box[5] == box[8]:
        return 1
    elif box[3] == box[6] and box[6] == box[9]:
        return 1

    #Transverse matching condition...
    elif box[1] == box[5] and box[5] == box[9]:
        return 1
    elif box[3] == box[5] and box[5] == box[7]:
        return 1

    #No matching condition...
    elif box[1]!= '1' and box[2]!= '2' and box[3]!= '3' and box[4]!= '4' and box[5]!= '5' and box[6]!= '6' and box[7]!= '7' and box[8]!= '8' and box[9]!= '9':
        return 0
    else:
        return -1

    #return 0

def markingBoard(choice, mark):
    if choice == 1 and box[1] == '1':
        box[1] = mark
        return True
    elif choice == 2 and box[2] == '2':
        box[2] = mark
        return True
    elif choice == 3 and box[3] == '3':
        box[3] = mark
        return True
    elif choice == 4 and box[4] == '4':
        box[4] = mark
        return True
    elif choice == 5 and box[5] == '5':
        box[5] = mark
        return True
    elif choice == 6 and box[6] == '6':
        box[6] = mark
        return True
    elif choice == 7 and box[7] == '7':
        box[7] = mark
        return True
    elif choice == 8 and box[8] == '8':
        box[8] = mark
        return True
    elif choice == 9 and box[9] == '9':
        box[9] = mark
        return True
    else:
        return False




                                          #Main Function


count = 0
player=1
name = []
print("")
print(f"        \033[91mWELCOME TO \033[92mTIC \033[93mTAC \033[94mTOE\033[0m")
print("")
print("        Game Mode:")
print("        1. Player vs Computer")
print("        2. Player vs Player")
print("")
mode = int(input("        Choose The Game Mode: "))
print('')
if mode == 1:
    print("        \033[94mYou Selected Player Vs Computer\033[0m")
    print("")
    name.append(input("        Enter the player name: ").upper())

    for _ in range(100):
        CreateBoard()
        player = 2 if player%2 == 0 else 1
        mark = 'X' if player == 1 else 'O'

        if player == 1:
            choice = int(input(f"{name[0]}, Enter a number: "))

            if choice == 1 and box[1] == '1':
                box[1] = mark
            elif choice == 2 and box[2] == '2':
                box[2] = mark
            elif choice == 3 and box[3] == '3':
                box[3] = mark
            elif choice == 4 and box[4] == '4':
                box[4] = mark
            elif choice == 5 and box[5] == '5':
                box[5] = mark
            elif choice == 6 and box[6] == '6':
                box[6] = mark
            elif choice == 7 and box[7] == '7':
                box[7] = mark
            elif choice == 8 and box[8] == '8':
                box[8] = mark
            elif choice == 9 and box[9] == '9':
                box[9] = mark

            else:
                print(RED + "Invalid Move. Try again." + RESET)
                player -= 1

        if player == 2:
            print("Computer, Enter : ",end="")

            if box[5] == '5':
                box[5] = mark
                print(5)
                count = 1
            elif box[5] != '5' and count == 0:
                count = 1
                for _ in range(1000):
                    n = random.randint(1,9)
                    if n%2 != 0 and n != 5:
                        box[n] = mark
                        print(n)
                        break

            elif comp_win():
                pass
            elif block_user():
                pass

            else:
                for _ in range(10):
                    n = random.randint(1,9)
                    if box[n] != 'X' and box[n] != 'O':
                        box[n] = mark
                        print(n)
                        break


        i = checkWinner()
        player += 1

        if i == 1 or i == 0:
            CreateBoard()
            break

    if i == 1:
        print(f"{name[0]} You Have Won The Game" if (player-1)%2 != 0 else "Computer Won The Game")
    else:
        print("Game Draw")

elif mode == 2:
    print("        \033[95mYou selected Player vs Player\033[0m")
    print("")
    name.append(input("        Enter the 1st player name: ").upper())
    name.append(input("        Enter the 2nd player name: ").upper())

    for _ in range(100):
        CreateBoard()
        player = 2 if player % 2 == 0 else 1
        mark = 'X' if player == 1 else 'O'

        while True:
            choice = int(input(f"{name[player-1]}! Enter a number: "))
            if markingBoard(choice, mark):
                break
            else:
                print(RED + "Invalid Move. Try again." + RESET)

        i = checkWinner()
        player += 1

        if i == 1 or i == 0:
            CreateBoard()
            break

    if i == 1:
        print(f"{name[0 if (player - 1) % 2 != 0 else 1]} You Have Won The Game")
    else:
        print("Game Draw")

else:
    print(RED + "Invalid Choice. Try again." + RESET)



