import time
import random
from fileInteraction import LoadEndings

NAME = "HEARTSTRING HIGH"

def typeWrite(message, addNewLine=True, endOfLinePause = 0.75):
    for i,char in enumerate(message):
        print(char, end='', flush=True)
        if char == '.':
            section = message[i-2:i+3]
            if section.count('.') >= 3:
                time.sleep(0.75)
        elif not char in [' ', '\n']:
            time.sleep(random.randint(3,14)/100)

    if addNewLine == True:
        time.sleep(endOfLinePause)
        print()

def getNumberInput(Min, Max):
    while True:
        typeWrite("--> ", False, 0)
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
    typeWrite(prompt, True, 0)
    print()
    for i, choice in enumerate(args):
        typeWrite(f"{i+1}) {choice}", True, 0)
    
    number = getNumberInput(1, len(args))
    print()
    return number

def typeAskNum(prompt, Min=0, Max=4):
    typeWrite(prompt, True, 0)
    return getNumberInput(Min, Max)

def newGameDialogue():
    typeWrite("Xingping, Yangshuo, China | 05/02/25 - 20:10 UTC+8")
    typeWrite("Chuhao walks along a dimmly lit allyway... 2 shadowy figures follow closely behind.")
    typeWrite("He walks around a corner onto a wider street where the dazzling white lights of a Ford Transit T-350 blind him.")
    typeWrite("The vehicle doesnt slow for the frozen Chuhoa as the 3.5 tonne van slams into his body.")
    typeWrite("...")
    typeWrite("The two figures move out of the shadows to quickly and efficiently move his chinese body into the back of the now blood stained van.")
    time.sleep(3)
    print()
    print()
    print()
    typeWrite("Caistor, Lincolnshire, England | 06/02/25 - 08:45 UTC+0")
    typeWrite("Chuhao awakes slowly tied to a chair in a clean tidy office. On the wall, hangs a clock and several peices of artwork.")
    typeWrite("Suddenly the door slams open and an angry scottish woman enters accompanied with a small bedraggled man dressed in all black.")
    typeWrite("The woman takes her place behind the desk infront of Chuhao glaring intensly at him")

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
    
    choice = typeAskSelection("Choose Your Action:",
                              "Start new game",
                              "Load game",
                              "View endings")
    if choice == 1:
        newGameDialogue()
    elif choice == 2:
        pass
    elif choice == 3:
        displayEndings()
    
main()