def BinarySearch(arr ,start, end,  target):
    
    mid = start + (end - start) // 2

    if arr[mid] == target:
        return mid 

    if start <= end:
        if arr[mid] > target and arr[start] < target:
            end = mid -1 
            return BinarySearch(arr ,start, end,  target)
        
        else:
            start = mid + 1
            return BinarySearch(arr ,start, end,  target)

    return -1 


if __name__ == '__main__':
    arr = [-1,0,2,3,6,7,8]
    target = 11
    start = 0 
    end = len(arr) -1 
    
    result = BinarySearch(arr, start, end, target)
    print(result)