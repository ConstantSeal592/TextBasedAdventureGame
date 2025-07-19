import json
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

# SaveNewEnding('Evil', 'Lewis', 100)
# print(LoadEndings())