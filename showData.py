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
        with open('NotesList.csv', 'r') as file:
            min = 0
            minTime = datetime.now()
            idList = []
            for line in file:
                min += 1
            # for line in file:
            #     if line.split(',')[0] == 'ID':
            #         continue
            #     if line.split(',')[1] < minTime:
            #         minTime = line.split(',')[1]
            #         idList[0] = line.split(',')[0]
            #     else:
            #         idList.append(line.split(',')[0])

            # ПРОДУМАТЬ СОРТИРОВКУ

            for line in file:

                print(line.split(',')[0], ' | ', line.split(',')[
                      1], ' | ', line.split(',')[2], ' | ', line.split(',')[3])
    except FileNotFoundError:
        print('No notes found')


def ShowSpecificNote(id):
    try:
        with open('NotesList.csv', 'r') as file:
            for line in file:
                i = 0
                if line.split(',')[0] == 'ID':
                    i = 0
                else:
                    i = int(line.split(',')[0])
                if i == id:
                    print(line.split(',')[0], ' | ', line.split(',')[
                          1], ' | ', line.split(',')[2], ' | ', line.split(',')[3])
            else:
                print(f'Note #{id} was not found')
    except FileNotFoundError:
        print('No notes found')
