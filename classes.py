import random

class Student:
    def __init__(self,data) -> None:
        self.affection = 0
        self.create(data)

    def create(self,data):
        self.name = data[0]
        self.description = data[1]
        self.interests = data[2]
        self.dialogue = data[3:]

    def response(self,id):
        response,reaction = self.dialogue[id].split("¦")
        return response,reaction
    
    def __repr__(self) -> str:
        return f"Obj: {self.name}"
    
class Dialogue:
     def __init__(self) -> None:
         self.dialogue = {
             
         }
         self.getDialogue()
     def getDialogue(self):

        with open("dialogue.txt","r") as file:
            text = file.read()
            text = text.split("&")[1:]
            for i,option in enumerate(text):
                text[i] = option.split("\n")[1:] # type: ignore   

        for i in range(len(text)):
            data = text[i]
            self.dialogue[f"{data[0]}"] = data[1:]
            print(f"{data[0]}")
        print(self.dialogue)
    
     def tryDialogue(self,id,student):
        print(self.dialogue[id][0])
        response,reaction = student.response(id)
        print(response)
        student.affection += reaction
        if reaction < 0:
            print(f"{student.name}'s affection has lowered by {reaction}")
        else:
            print(f"{student.name}'s affection has raised by {reaction}")
        
    
class Player:
    def __init__(self) -> None:
        self.inventory = []
        self.focus = 5
        self.grades = ["A","A","A","A"]


    def interact(self,action):
        #perform(action)


        self.focus -=1
        if self.focus == 0:
            return False
        return True
    

class Item:
    def __init__(self,name,description,effect) -> None:
        self.Name = name
        self.info = description
        self.effect = effect

    def use(self):
        return eval(self.effect)
    

class Classroom:
    def __init__(self,player) -> None:
        self.students = [player]
        self.seating = []
        self.createStudents()
        self.createSeating()

    def createStudents(self):
        with open("Students.txt","r") as file:
            text = file.read()
            text = text.split("&")[1:]
            for i,person in enumerate(text):
                text[i] = person.split("\n")[1:] # type: ignore   

        for i in range(len(text)):
            data = text[i]
            self.students.append(Student(data))
            

    def createSeating(self):
        classSize = len(self.students)
        arrLen = int(str((classSize**0.5))[0]) + 1
        random.shuffle(self.students)
        

        for i in range(arrLen):
            temp = []
            for j in range(arrLen):
                try:
                    temp.append(self.students[j+ i*arrLen])
                    #print(self.students[j+ i*arrLen].dialogue) 
                except:
                    temp.append(None)
            self.seating.append(temp)
        print(self.seating)
                
                


player = Player()
speech = Dialogue()
c3 = Classroom(player)

