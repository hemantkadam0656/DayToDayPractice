def IsValid(arr, n, m, mid):
    ptrs = 1 
    time = 0
    
    for i in range(n):
        #  [1,3,2,4]
        # mid = 5
        # mid = 8
        if arr[i] > mid :
            return False 
        
        if (time + arr[i]) <= mid:
            time += arr[i]
        else:
            time = arr[i] 
            ptrs += 1

    # for mid 5 the possible answers == 4 2 4 which is exceeded the limit of ptrs
    
    if ptrs > m:
        # print(ptrs, "False")
        return False  
    else:
        return True
        
   
def PainterPatition(arr, n, m):
    start =  0 
    end = sum(arr)

    while start <= end:
        mid = start + (end - start) // 2
        # mid  = 6 + (10 - 6) // 2 == 6 + 2 == == 8 
        # mid = 6 + (7 - 6 ) // 2 == 6 + 1 == 7
        # mid = 6 + (6 - 6)//2 == 6
 
        if IsValid(arr, n, m, mid):
            end = mid - 1
        else:
            start = mid + 1

    return mid

if __name__ == "__main__":   
    n = 4
    m = 2
    arr = [1,3,2,4]
    res = PainterPatition(arr, n, m)
    print(res)


    # 0 1 2 3 4 5 6 7 8 9  

    # p1 = 1  p2 = 9
    # p1 = 4  p2 = 6
    # p1 = 6  p2 = 4 
    
    


