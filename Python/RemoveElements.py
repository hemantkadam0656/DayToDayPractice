def RemoveElements(num, val):
    lst = num
    n = len(num) # 8
    i,j = 0,0
    while i < n - j:
        if lst[i] == val:
            lst[n-1-j] = lst[i]
            j += 1
            i += 1
        else:
            i += 1
    return lst
            
    


num = [0,1,2,2,3,0,4,2]
val = 2
print(RemoveElements(num, val))

