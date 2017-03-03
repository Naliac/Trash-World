from copy import copy

def commaCode(theList):
    theListCopy = copy(theList) # copy of the original list, just incase
    rValue = '' 
    for ind in range(len(theListCopy)):
        if ind == len(theListCopy) -1: 
            rValue += 'and '            
            rValue += str(theListCopy[ind])
            break
        rValue += str(theListCopy[ind])
        rValue += ', '
    return rValue # aha! there now it works with all kinds of lists!
                    # *insert evil laugh*...it still looks like shit


ListValues = ['winky face', 4.04, 69, '100% serious', 'roadhog', 'junkrat']
result = commaCode(ListValues)
print(type(result))
print(result)

