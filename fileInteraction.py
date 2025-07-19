import json,pickle
import datetime

def LoadEndings():
    link = open('Endings.txt', 'r')
    data = link.read()
    link.close()

    endings = []

    for entry in data.split('\n'):
        if entry != '':
            endings.append(json.loads(entry))

    return endings

def SaveNewEnding(EndingName, DateName, AvgGrade):
    link = open('Endings.txt', 'a')
    link.write(json.dumps({
        'EndingName': EndingName,
        'Time': str(datetime.datetime.now())[:10],
        'DateName': DateName,
        'AvgGrade': AvgGrade
    }) + '\n')


def saveClass(object,component):
    with open(f'{component}.pkl', 'wb') as f:
        pickle.dump(object, f)

def saveAll(plr,StudentList,Classes):
    saveClass(plr,"player")
    saveClass(StudentList,"studentList")
    saveClass(Classes,"classes")

def loadAll():
    with open(f'{"player"}.pkl', 'rb') as f:
        player = pickle.load(f)
    with open(f'{"studentList"}.pkl', 'rb') as f:
        students = pickle.load(f)
    with open(f'{"classes"}.pkl', 'rb') as f:
        classes = pickle.load(f)
    return player,students,classes
# SaveNewEnding('Evil', 'Lewis', 100)
# print(LoadEndings())