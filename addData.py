def EnterNoteData():
    from datetime import datetime
    id = 0
    try:
        with open('NotesList.csv', 'r') as file:
            for line in file:
                id = line.split(',')[0]
        if id == 'ID':
            id = 1
        else:
            id = int(id) + 1
        time = datetime.now()
        noteSubject = input('Enter subject ')
        noteBody = input('Enter Note Body ')
        with open('NotesList.csv', 'a') as file:
            file.write(f'\n{id},{time},{noteSubject},{noteBody}')
    except FileNotFoundError:
        with open('NotesList.csv', 'w') as file:
            file.write(f'ID,Time,Subject,Body\n')
        id = 1
        time = datetime.now()
        noteSubject = input('Enter subject ')
        noteBody = input('Enter Note Body ')
        with open('NotesList.csv', 'a') as file:
            file.write(f'{id},{time},{noteSubject},{noteBody}')


def NoteAmend(id):
    import os
    from datetime import datetime
    flag = False
    with open('NotesList.csv', 'r') as file:
        for line in file:
            i = 0
            if line.split(',')[0] == 'ID':
                i = 0
            else:
                i = int(line.split(',')[0])
            if i == id:
                idTmp = id
                time = datetime.now()
                noteSubject = input('Enter new subject\n')
                noteBody = input('Enter new body\n')
                with open('tmp.csv', 'a') as file1:
                    file1.write(f'{idTmp},{time},{noteSubject},{noteBody}\n')
                flag = True
                print(f'Note #{id} was updated')
            else:
                idTmp = line.split(',')[0]
                time = line.split(',')[1]
                noteSubject = line.split(',')[2]
                noteBody = line.split(',')[3]
                with open('tmp.csv', 'a') as file1:
                    file1.write(f'{idTmp},{time},{noteSubject},{noteBody}')
    if flag == True:
        os.remove('NotesList.csv')
        os.rename('tmp.csv', 'NotesList.csv')
    else:
        print(f'Note #{id} was not found')
        os.remove('tmp.csv')

def NoteDelete(id):
    import os
    flag = False
    with open('NotesList.csv', 'r') as file:
        for line in file:
            i = 0
            if line.split(',')[0] == 'ID':
                i = 0
            else:
                i = int(line.split(',')[0])
            if i != id:
                idTmp = line.split(',')[0]
                time = line.split(',')[1]
                noteSubject = line.split(',')[2]
                noteBody = line.split(',')[3].rstrip()
                with open('tmp.csv', 'a') as file1:
                    if i == 0:
                        file1.write(f'{idTmp},{time},{noteSubject},{noteBody}')
                    else:    
                        file1.write(f'\n{idTmp},{time},{noteSubject},{noteBody}')
            if i == id:
                flag = True
    if flag == True:
        os.remove('NotesList.csv')
        os.rename('tmp.csv', 'NotesList.csv')
    else:
        print(f'Note #{id} was not found')
        os.remove('tmp.csv')
