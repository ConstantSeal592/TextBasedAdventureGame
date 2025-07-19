import time
import random
from fileInteraction import LoadEndings

NAME = "HEARTSTRING HIGH"

def typeWrite(message, addNewLine=True):
    for char in message:
        print(char, end='', flush=True)
        if not char in [' ', '\n']:
            time.sleep(random.randint(2,14)/100)

    if addNewLine == True:
        print()

def getNumberInput(Min, Max):
    while True:
        typeWrite("--> ", False)
        userInput = input()
        print()

        try:
            num = int(userInput)
            if num >= Min and num <= Max:
                return num
            else:
                typeWrite(f"Please Enter a number in the range {Min} to {Max}")
        except:
            typeWrite("Please Enter an integer number")

def typeAskSelection(prompt, *args):
    typeWrite(prompt)
    print()
    for i, choice in enumerate(args):
        typeWrite(f"{i+1}) {choice}")
    
    number = getNumberInput(1, len(args))
    print()
    return number

def typeAskNum(prompt, Min=0, Max=4):
    typeWrite(prompt)
    return getNumberInput(Min, Max)

SQUARESIDES = 5
def displayEndings():
    endings = LoadEndings()

    typeWrite('Endings:')
    print()
    for ending in endings:
        print('# '*SQUARESIDES)
        for i in range(0, SQUARESIDES-2, 1):
            if i == (SQUARESIDES - 2)//2:
                print('#' + ending['EndingName'].center(SQUARESIDES*2 - 3) + '#' + ' '*4 + f"Date: {ending['DateName']}")
            elif i == (SQUARESIDES - 2)//2 - 1:
                print('#' + ' '*((SQUARESIDES-2)*2 + 1) + '#' + ' '*4 + f"Time: {ending['Time']}")
            elif i == (SQUARESIDES - 2)//2 + 1:
                print('#' + ' '*((SQUARESIDES-2)*2 + 1) + '#' + ' '*4 + f"Average Grade: {ending['AvgGrade']}")
            else:
                print('#' + ' '*((SQUARESIDES-2)*2 + 1) + '#')        
        print('# '*SQUARESIDES)
        print()

def main():
    print('\n'.join([
            '#'*40,
            '',
            ' '*((40-len(NAME))//2) + NAME,
            '',
            '#'*40
        ]))
    
    choice = 3
    # choice = typeAskSelection("Choose Your Action:",
    #                           "Start new game",
    #                           "Load game",
    #                           "View endings")
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        displayEndings()
    
main()