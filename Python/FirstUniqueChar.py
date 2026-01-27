def  FirstUniqueChar(s):
    count = {}
    n = len(s)
    char = ""

    for i in range(n):
        count[s[i]] = count.get(s[i], 0) + 1
        
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
        
    return -1 

if __name__ == '__main__':
    s = "aabb"
    res = FirstUniqueChar(s)
    print(res)
