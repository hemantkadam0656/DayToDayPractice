# using sorting method to find Kth largest element

def KthLargestNum(arr,k):
    n = len(arr)
    i = 0

    if k >= n :
        return -1 
    
    while i < n :
        for j in range(i+1, n):
            if arr[i]> arr[j]:
                arr[j], arr[i] = arr[i], arr[j]  
        
        i+=1
    
    return arr[k]
    

def duplicateKthLargestNum(arr, k):
    n = len(arr)
    i = 0

    if k >= n :
        return -1 
    
    while i < n :
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]  

        i+=1

    if k == 1 :
        arr[0]
    
    for i in range(2,):
        if arr[i] == arr[i -1]:
            kthEle = arr[i]

    return arr


if __name__ == '__main__':
    arr = [1, 14, 2, 16, 10, 20, 20, 21, 19, 18]
    k = 6
    res = KthLargestNum(arr, k)
    res2 = duplicateKthLargestNum(arr, k)
    print(res)
    print(res2)