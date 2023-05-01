def AddGetSelection():
    promptText = 'Select: \n1 - to add New Note, \
                              \n2 - to see list of Notes, \
                              \n3 - to see one particular Note \
                              \n4 - to change existing Note, \
                              \n5 - to delete a Note, \
                              \n6 - exit. \n'

    selection = GetIntInput(promptText)
    while selection not in [1, 2, 3, 4, 5, 6]:
        selection = GetIntInput(promptText)
    return selection


def GetIntInput(inputText):
    b = 0
    a = input(inputText)
    while b != 1:
        if a.isnumeric():
            b = 1
            return int(a)
        else:
            a = input(inputText)
