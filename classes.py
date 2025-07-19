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
        print(id)
        response,reaction = self.dialogue[id-1].split("|")
        return response,int(reaction)
    
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
            text = text[:10]

        for i in range(len(text)):
            data = text[i]
            self.dialogue[f"{data[0]}"] = data[1]
            

     def tryDialogue(self,id,student):
        response,reaction = student.response(int(id))
        student.affection += reaction
        return response, reaction
        
    
class Player:
    def __init__(self) -> None:
        self.inventory = []
        self.focus = 5


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
    def __init__(self, subject, player, StudentList) -> None:
        self.subject = subject
        self.grade = 75     #Max 100, Min 0
        self.player = player
        self.students = [player] + StudentList.copy()
        self.seating = []
        self.createSeating()
        self.GetAdjStudents()

    def getGradeValue(self):
        if self.grade < 8:
            return 'U'
        elif self.grade < 14:
            return 'F'
        elif self.grade < 25:
            return 'E'
        elif self.grade < 37:
            return 'D'
        elif self.grade < 48:
            return 'C'
        elif self.grade < 65:
            return 'B'
        elif self.grade < 85:
            return 'A'
        elif self.grade < 93:
            return 'A*'
        
    def GetAdjStudents(self):
        temp = []
        x,y = divmod(self.playerPos,(int(str((len(self.students)**0.5))[0])+1))
        print(x,y)
        try:
            temp.append(self.seating[x+1][y])
        except:
            pass
        try:
            temp.append(self.seating[x-1][y])
        except:
            pass
        try:
            temp.append(self.seating[x][y+1])
        except:
            pass
        try:
            if self.seating[x][y-1] == self.player:
                pass
            else:
                temp.append(self.seating[x][y-1])
        except:
            pass
        print(temp)
        return temp
        
        
        
    def createSeating(self):
        classSize = len(self.students)
        arrLen = int(str((classSize**0.5))[0]) + 1
        random.shuffle(self.students)
        for i in range(len(self.students)):
            if self.player == self.students[i]:
                self.playerPos = i
        for i in range(arrLen):
            temp = []
            for j in range(arrLen):
                try:
                    temp.append(self.students[j+ i*arrLen])
                    #print(self.students[j+ i*arrLen].dialogue) 
                except:
                    pass
            self.seating.append(temp)

                
def createStudents():
    studentList = []
    with open("Students.txt","r") as file:
        text = file.read()
        text = text.split("&")[1:]
        for i,person in enumerate(text):
            text[i] = person.split("\n")[1:] # type: ignore   

    for i in range(len(text)):
        data = text[i]
        studentList.append(Student(data))                
    return studentList

def InstantiateObjects():
    plr = Player()
    StudentList = createStudents()
    Classes = [(Classroom(sub, plr, StudentList)) for sub in ["Physics", "Maths", "Further Maths", "Physics"]]
    dialogue = Dialogue()
    return plr, StudentList, Classes, dialogue 

player, students, Classes, dialogue = InstantiateObjects()
# dialogue.tryDialogue("4",students[1])