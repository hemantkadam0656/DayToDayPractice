# This examples is related to array binary search for thr sorted but rotated array. 
# To find the given target from array I suppose to apply the binary sort on two sub arrays. 
# if target lies in first sub-array, it means the second half is sorted and I need to apply BS on first half. 
# if target is not in first half it means that is in second half, so I need to apply BS to second half.

def SortedRotatedArray(arr, target):
    start = 0 
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid 
        
        # check which part of array is sorted (left or right)
        # if you array start is less than mid it means your left part is sorted  [3,4,5,6,7,0,1,2] --> mid == 7 --> 3 < 7
        # if not it means a second part of array right part is sorted  [6,7,0,1,2,3,4,5] --> mid == 2 -->  6 > 2 
         
        if arr[start] <= arr[mid]: # left part is sorted 
            if arr[start] < target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:                       # right part is sorted 
            if arr[mid] < target < arr[end]:
                start = mid + 1
            else:
                end = mid-1 
    
    return -1 


if __name__ == "__main__":
    arr = [3,4,5,6,7,0,1,2]
    target = 0
    res = SortedRotatedArray(arr, target)
    print(res)







