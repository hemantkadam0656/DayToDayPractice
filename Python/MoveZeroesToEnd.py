# Question:- Move all zeros to the end while maintaining order?

# Steps:-
# 
# 

def MoveAllZeroesToEnd(arr):
    n = len(arr)
    start = 0
    end = 1

    while end < n:
        if arr[start] == 0 and arr[end] != 0:
            arr[start], arr[end] = arr[end], arr[start]

        elif arr[start] == 0 and arr[end] == 0:
            end +=1 
        
        else:
            start +=1
            end += 1
    
    return arr

def BestApproch(arr):
    pos = 0 
    n = len(arr)

    for num in arr:
        if arr != 0:
            arr[pos] = num
            pos += 1
    

    for i in range(pos, n):
        arr[i] = 0 
    
    return arr



if __name__ == '__main__':
    arr =  [0, 1, 0, 2, 3]
    res = MoveAllZeroesToEnd(arr)
    best = BestApproch(arr)
    print(best)
    print(res)

