import view as v
import addData as add
import showData as show


def Start():
    a = v.AddGetSelection()
    if a == 1:
        add.EnterNoteData()
    elif a == 2:
        i = v.GetIntInput(
            '1 - to see Notes sorted by ID\n2 - to see notes sorted by Time\n')
        while i not in [1, 2]:
            i = v.GetIntInput(
                '1 - to see Notes sorted by ID\n2 - to see notes sorted by Time\n')
        if i == 1:
            show.ShowNotes()
        else:
            show.ShowNotesTimeFilter()
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
