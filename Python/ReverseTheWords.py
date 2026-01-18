def ReverseTheWords(s):
    strList = s.split()
    i = 0 
    j = len(strList)-1 

    while i <= j:
        strList[i], strList[j] = strList[j], strList[i]
        i += 1
        j -= 1
    
    s = ' '.join(strList)

    return s


if __name__ == '__main__':
    s = "Hello World from Python"
    res = ReverseTheWords(s)
    print(res)