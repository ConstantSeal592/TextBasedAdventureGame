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
    data = {
        'EndingName': EndingName,
        'Time': str(datetime.datetime.now())[:10],
        'DateName': DateName,
        'AvgGrade': AvgGrade
    }
    link.write(json.dumps(data) + '\n')

    return data


def saveClass(object,component):
    with open(f'{component}.pkl', 'wb') as f:
        pickle.dump(object, f)

def saveAll(day,plr,StudentList,Classes):
    saveClass(day,'meta')
    saveClass(plr,"player")
    saveClass(StudentList,"studentList")
    saveClass(Classes,"classes")

def loadAll():
    try:
        with open(f'{"meta"}.pkl', 'rb') as f:
            day = pickle.load(f)
        with open(f'{"player"}.pkl', 'rb') as f:
            player = pickle.load(f)
        with open(f'{"studentList"}.pkl', 'rb') as f:
            students = pickle.load(f)
        with open(f'{"classes"}.pkl', 'rb') as f:
            classes = pickle.load(f)
        return day,player,students,classes
    except:
        return None,None,None,None
# SaveNewEnding('Evil', 'Lewis', 100)
# print(LoadEndings())