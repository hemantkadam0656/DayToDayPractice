def Isvalid(arr,n,m, mid):
    pages = 0 
    student = 1

    for i in range(n):
        if arr[i] > mid:
            return False
        
        if pages+ arr[i] <=  mid:
            pages += arr[i]
        else:        
            student+= 1
            pages = arr[i]
        
    if student > m:
        return False
    else:
        return True
        

def BookAllocation(arr, n, m):
    start = 0 
    end = sum(arr)

    if m > n:
        return -1 
    
    while start <= end:
        mid = start + (end - start)// 2

        if Isvalid(arr,n,m, mid ):
            end = mid - 1
        else:
            start = mid + 1
    
    return mid 


if __name__ == '__main__':
    arr = [15,17,20]
    m = 2
    n = 3
    res = BookAllocation(arr, n, m)
    print(res)





