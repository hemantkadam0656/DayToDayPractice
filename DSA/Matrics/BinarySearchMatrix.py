# search in 2D matrix

# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16 

# The time complexity for the below code is O(log m * n) == O(log m + log n) 
# The below binary search applied row wise and then column wise search. which helps us to find target value in sorted array.
# Note:- array is row wise sorted as well as the next starting element of row is always greter that it previous. 

def BinarySearch(arr, target):
    m = len(arr)
    n = len(arr[0])

    start = 0
    end = m-1 

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid][0] <= target <= arr[mid][n-1]:
            start = 0
            end = len(arr[mid]) -1 

            while start <= end:
                mid2= start + (end - start) // 2
                
                if arr[mid][mid2] == target:
                    return (mid, mid2)
                elif target > arr[mid][mid2]:
                    start = mid2 + 1
                else:
                    end = mid2 - 1
            
        elif target > arr[mid][n-1]:
            start = mid + 1
        else:
             end = mid -1 

    return (-1,-1)

if __name__ == '__main__':
    arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    target = 9
    res = BinarySearch(arr, target)
    print(res)

