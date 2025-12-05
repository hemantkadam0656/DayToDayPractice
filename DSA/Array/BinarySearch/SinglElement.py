
def FindSingleElement(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2
        # 8 = arr[8] ==5 

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid + 1]:
            return arr[mid] 
        
        if arr[mid] == 0 and arr[mid+1] != arr[mid]:
            return arr[mid]

        if arr[mid] == len(arr) -1 and arr[mid] != arr[mid -1]:
            return arr[mid]

        if mid%2 == 0: # if mid is even
            if arr[mid] == arr[mid -1]:
                end = mid-1 
            else:
                start = mid+1
        else: # if mid is odd
            if arr[mid] == arr[mid-1]:
                start = mid+1 
            else:
                end = mid-1 
    
    return -1

if __name__ == "__main__":
    arr = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9]
    res = FindSingleElement(arr)
    print(res)
