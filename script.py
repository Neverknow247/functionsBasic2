def countdown(num):
    list = []
    for i in range(num,-1,-1):
        list.append(i)
    return list

def printAndReturn(_list):
    print(_list[0])
    return(_list[1])

def firstPlusLength(_list):
    return(_list[0]+len(_list))

def valuesGreaterThanSecond(_list):
    list = []
    if len(_list)<2:
        return(False)
    else:
        for i in range(len(_list)):
            if _list[i] > _list[1]:
                list.append(_list[i])
        print(len(list))
        return(list)

def thisLengthThatValue(_len,_val):
    list = []
    for i in range(_len):
        list.append(_val)
    print(list)

countdown(5)
printAndReturn([1,2])
firstPlusLength([1,2,3,4,5])
valuesGreaterThanSecond([5,2,3,2,1,4])
thisLengthThatValue(4,7)