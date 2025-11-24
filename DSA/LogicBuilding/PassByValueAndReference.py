# Pass By Value 
def PassByValue(a):
    a = a + 10 
    print('Inside PassByValue Function :', a)

if __name__ ==  '__main__':
    a = 5
    res = PassByValue(a)
    print('Outside of PassByValue function :', a)


def PassByRefence(myList):
    myList[0] = 100
    print('Inside PassByRefence function :', myList)


if __name__ == '__main__':
    myList = [11,12,13,14,15]
    result = PassByRefence(myList)
    print('Outside of PassByRefence function :', myList)





