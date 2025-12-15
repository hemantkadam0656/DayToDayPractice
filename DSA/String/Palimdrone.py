def Palimdrone(string):
    LowerStr = string.lower()
    i = 0 
    j = len(string)-1

    while i <= j:
        if LowerStr[i] == LowerStr[j]:
            i += 1
            j -= 1
        else:
            return False 
    
    return True 
     
if __name__ == '__main__':
    string = 'racecar'
    res = Palimdrone(string)
    print(res)




