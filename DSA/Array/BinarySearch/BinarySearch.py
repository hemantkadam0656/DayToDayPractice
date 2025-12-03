# to avoid overflow error for caluculate mid in platform like leetcode, etc
# we are changing our formula  (start + end ) // 2 into the [ start + (start - end ) // 2 ]
# This is normal loop method


def BinarySearch(arr, target):
    end = len(arr)-1 
    start = 0

    while start <= end:
        mid =  start + (end  - start) // 2 
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid

    return -1  
  

if __name__ == "__main__":
    arr = [-1,0,3,4,5,6,9,12]
    target = 0
    res = BinarySearch(arr, target)
    print(res)


# Binary search using Recursion method

def BinarySearchByRecursion(arr, target, start = None, end = None):
    
    if start is None:
        start = 0
    if end is None:
        end = len(arr)-1 

    if start > end:
        return -1
    
    arrmid =  start + (end  - start) // 2 
    if target > arr[arrmid]:
        return BinarySearchByRecursion(arr, target, arrmid + 1, end)
    elif target < arr[arrmid]:
        return BinarySearchByRecursion(arr, target, start , arrmid - 1)
    else:
        return arrmid

    
  

if __name__ == "__main__":
    arr = [-1,0,3,4,5,6,9,12]
    target = 0
    res = BinarySearchByRecursion(arr, target)
    print(res)









