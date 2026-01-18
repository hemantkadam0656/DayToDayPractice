def  ValidAnagram(s,t):
    if len(s) != len(t):
        return False

    freqWord = {}

    for i in s:  
        freqWord[i] = freqWord.get(i, 0) + 1
    
    print(freqWord)
    for j in t:
        if j not in freqWord:
            return False 
        
        freqWord[j] -= 1
    
    print(freqWord)
    for z in freqWord.values():
        if z != 0:
            return False

    return True 
  
if __name__ == '__main__':
    s = "blabla" 
    t = "blabaa"
    res = ValidAnagram(s,t)
    print(res)