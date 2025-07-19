import time
import random
from fileInteraction import LoadEndings,SaveNewEnding,saveAll,loadAll
from classes import InstantiateObjects,getGradeValue

NAME = "HEARTSTRING HIGH"
DEBUGMODE = True

FOCUSPHRASES = ["You lock in"]

def typeWrite(message, addNewLine=True, endOfLinePause = 0.75):
    for i,char in enumerate(message):
        print(char, end='', flush=True)
        if char == '.':
            section = message[i-2:i+3]
            if section.count('.') >= 3:
                if DEBUGMODE == False:
                    time.sleep(0.75)
        elif not char in [' ', '\n']:
            if DEBUGMODE == False:
                time.sleep(random.randint(3,14)/100)

    if addNewLine == True:
        if DEBUGMODE == False:
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
    typeWrite("The woman: 'My name is Mrs Buck, and if you dont get a date by the end of the week, he will lynch you!' gesturing to the man in black")
    time.sleep(3)
    print()
    typeWrite("Chuhao is then dragged out of the office and escourted to his first lesson...")
    print('\n\n')

    game(0, *InstantiateObjects())

SQUARESIDES = 5
def printEnding(ending):
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


def displayEndings():
    endings = LoadEndings()

    typeWrite('Endings:')
    print()
    for ending in endings:
        printEnding(ending)


def getRandID(usedIDs, IDs, dialogue):
    while True:
        rand = random.randint(1, len(dialogue.dialogue))

        used = False
        for i in range(0, len(IDs), 1):
            if rand == IDs[i][0]:
                used = True
                break

        if rand in usedIDs or used == True:
            continue
        else:
            return rand
        
def calcAvgGrade(classes):
    total = 0
    for sub in classes:
        total += sub.grade
    
    total /= len(classes)

    return getGradeValue(total)

def game(day, plr, studentList, classes, dialogue):
    usedIDs = []
    for d in range(day,3,1):
        typeWrite(f"Day {d+1}...")
        for subject in classes:
            typeWrite(f"You enter {subject.subject}...")
            print()

            actions = 3
            while actions > 0:
                IDs = []
                for i in range(0,3,1):
                    ID = getRandID(usedIDs, IDs, dialogue)
                    usedIDs.append(ID)
                    if len(usedIDs) == len(dialogue.dialogue):
                        usedIDs = []
                    
                    IDs.append([str(ID), random.choice(subject.GetAdjStudents())])

                choice = typeAskSelection("Choose an action to take:",
                                        f"{dialogue.dialogue[IDs[0][0]]} to {IDs[0][1].name}",
                                        f"{dialogue.dialogue[IDs[1][0]]} to {IDs[1][1].name}",
                                        f"{dialogue.dialogue[IDs[2][0]]} to {IDs[2][1].name}",
                                        "Focus on work")
                
                if choice == 4:
                    subject.grade += random.randint(5,8)
                    subject.grade = min(100,max(0,subject.grade))

                    typeWrite(random.choice(FOCUSPHRASES))

                else:
                    choice = IDs[choice-1]
                    responce, reaction = dialogue.tryDialogue(*choice)
                    typeWrite(f"{choice[1].name}: {responce}")
                    typeWrite(f"{choice[1].name}'s affection has changed by {reaction}")

                    subject.grade -= random.randint(6,7)
                    subject.grade = min(100,max(0,subject.grade))
                
                print('\n')

                actions -= 1

        saveAll(d,plr,studentList,classes)

        typeWrite("You reflect on the day...")
        typeWrite("Name".ljust(20)+'|'+"Affection")
        typeWrite('-'*20+'+'+'-'*10)
        for student in studentList:
            typeWrite(student.name.ljust(20)+'|'+str(student.affection))
        print('\n\n\n')

    typeWrite("Chuhao's time has come... Mrs Buck will lynch him if he couldnt go out on a date")
    typeWrite("But would anyone say yes?...")

    Names = []
    for student in studentList:
        Names.append(student.name)

    choice = typeAskSelection("Who should Chuhao ask out?",*Names)

    typeWrite(f"Chuhao nervously walks up to {Names[choice-1]} just before they leave the gates...")
    typeWrite("Chuzzy asks them out...")

    target = None

    for student in studentList:
        if student.name == Names[choice-1]:
            target = student

    num = random.randint(1,10)
    success = num < target.affection

    typeWrite(f"They say...")
    typeWrite(f"... {'Yes' if success else 'No'}")

    if success and calcAvgGrade(classes) in ['U','F','E','D','C']:     #Fail
        typeWrite("Chuhao returns to Mrs Buck's office with a spring in his step")
        typeWrite("I hear you got a date says Mrs Buck, to which Chuhao vigorously nods")
        typeWrite("Well you managed it... but unfortunately your average grade was too low...")
        typeWrite("Therefore you are now obligated to go to Caistor Yarb3orough... good luck getting a date there")
        print('\n\n')
        typeWrite("You got the... Fail Ending!")
        
        data = SaveNewEnding('Fail', target.name, calcAvgGrade(classes))
        printEnding(data)
    elif success and target.name == 'Alex':     #Alex
        typeWrite("Chuhao returns to Mrs Buck's office with a spring in his step")
        typeWrite("Dont be so proud of yourself says Mrs Buck...")
        typeWrite("Alex said yes... Im sorry for you")
        print('\n\n')
        typeWrite("You got the... Alex Ending!")
        
        data = SaveNewEnding('Alex', target.name, calcAvgGrade(classes))
    elif success:     #Good
        typeWrite("Chuhao returns to Mrs Buck's office with a spring in his step")
        typeWrite("I hear you got a date says Mrs Buck, to which Chuhao vigorously nods")
        typeWrite("Well you managed it, so I suppose we will deport you, sighs Mrs Buck")
        print('\n\n')
        typeWrite("You got the... Good Ending!")
        
        data = SaveNewEnding('Good', target.name, calcAvgGrade(classes))
        printEnding(data)
    else:   #Bad
        typeWrite("Chuhao returns to Mrs Buck's office gloomily")
        typeWrite("HA! I knew no one would date you, screamed Mrs Buck!")
        typeWrite("Prepare... to be... castrated")
        print('\n\n')
        typeWrite("You got the... Bad Ending!")
        
        data = SaveNewEnding('Bad', target.name, calcAvgGrade(classes))
        printEnding(data)



def main():
    print('\n'.join([
          '#'*40,
          '',
          ' '*((40-len(NAME))//2) + NAME,
          '',
          '#'*40
    ]))
    
    running = True
    while running:
        
        choice = typeAskSelection("Choose Your Action:",
                                "Start new game",
                                "Load game",
                                "View endings",
                                "Quit")
        
        if choice == 1:
            newGameDialogue()
        elif choice == 2:
            plr, StudentList, Classes, dialogue = InstantiateObjects()
            if plr == None:
                typeWrite("No Valid Save")
                continue
            typeWrite("Save loaded")
            game(*loadAll(),dialogue)
        elif choice == 3:
            displayEndings()
        elif choice == 4:
            running = False
    
main()