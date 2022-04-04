def countdown(x):
    countlist = []
    for y in range(x,-1,-1):
        countlist.append(y)
    return countlist
print(countdown(7))

def printAndReturn(x):
    print(x[0])
    return x[1]
print(printAndReturn([1,2]))

def firstPlusLength(x):
    sum = x[0] + len(x)
    return sum
print (firstPlusLength([1,2,3,4,5,6,7]))

def valuesGreaterThanSecond(x):
    arr = []
    for y in range(0,len(x)):
        if x[y] > x[1]:
            arr.append(x[y])
    print(len(arr))
    return arr
print(valuesGreaterThanSecond([1,3,4,1,5,1,6]))

def length_and_value(a,b):
    arr = []
    for x in range(0,a):
        arr.append(b)
    return arr
print(length_and_value(4,7))