def ShowNotes():
    try:
        with open('NotesList.csv', 'r') as file:
            for line in file:
                print(line.split(',')[0], ' | ', line.split(',')[
                      1], ' | ', line.split(',')[2], ' | ', line.split(',')[3])
    except FileNotFoundError:
        print('No notes found')


def ShowNotesTimeFilter():
    from datetime import datetime
    try:
        idList = []
        with open('NotesList.csv', 'r') as file:
            for line in file:
                if line.split(',')[0] == 'ID':
                    print(line.split(',')[0], ' | ', line.split(',')[
                          1], ' | ', line.split(',')[2], ' | ', line.split(',')[3])
                else:
                    idList.append(line.split(',')[1])
            idList.sort()
        for i in idList:
            with open('NotesList.csv', 'r') as file:
                for line in file:
                    if i == line.split(',')[1]:
                        print(line.split(',')[0], ' | ', line.split(',')[
                              1], ' | ', line.split(',')[2], ' | ', line.split(',')[3])
    except FileNotFoundError:
        print('No notes found')


def ShowSpecificNote(id):
    try:
        with open('NotesList.csv', 'r') as file:
            flag = False
            for line in file:
                i = 0
                if line.split(',')[0] == 'ID':
                    i = 0
                else:
                    i = int(line.split(',')[0])
                if i == id:
                    print(line.split(',')[0], ' | ', line.split(',')[
                          1], ' | ', line.split(',')[2], ' | ', line.split(',')[3])
                    flag = True
            if flag == False:
                print(f'Note #{id} was not found')
    except FileNotFoundError:
        print('No notes found')
