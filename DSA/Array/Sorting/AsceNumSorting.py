
def AsceNumSorting(arr):
    n = len(arr)
    count0 = 0
    count1 = 0
    count2 = 0 

    for i in range(n):
        if arr[i] == 0:
            count0 +=1 
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    
    curr = 0
    # [0,1,2,2,2,1,1,1,0,0,0]
    for i in range(count0):
        arr[i] = 0

    curr += count0
    # [0,0,0,0,2,1,1,1,0,0,0]
    for i in range(count1):
        arr[curr + i] = 1
    
    curr  += count1
    for i in range(count2):
        arr[curr + i] = 2
    
    return arr



if __name__ == '__main__':
    arr = [0,1,2,2,2,1,1,1,0,0,0]
    res = AsceNumSorting(arr)
    print(res)



