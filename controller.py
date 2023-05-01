import view as v
import addData as add
import showData as show


def Start():
    a = v.AddGetSelection()
    if a == 1:
        add.EnterNoteData()
    elif a == 2:
        show.ShowNotes()
    elif a == 3:
        i = v.GetIntInput('Select Note ID to show\n')
        show.ShowSpecificNote(i)
    elif a == 4:
        show.ShowNotes()
        i = v.GetIntInput('Select Note ID to update\n')
        add.NoteAmend(i)
    elif a == 5:
        id = v.GetIntInput('Select Note ID to delete\n')
        add.NoteDelete(id)
    elif a == 6:
        print('Good bye!')
