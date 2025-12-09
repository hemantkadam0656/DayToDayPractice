# que :- Aggressive Cows – Problem Statement

# You are given an array arr[] of size N, where each element represents the position of a stall on a straight line.
# You are also given an integer C, the number of cows.

# Your task is to place the C cows in these stalls such that:

# The minimum distance between any two cows is as large as possible.

# Return the largest minimum distance.
# ------------------------------------------------------------------------------------------------------------------

# steps:- 
# To solve this question first of all we need to sort the array and lets suppose we have array(gothe) like 1-2-3-4-5-6-7-8-9
# So suppose, to find maximum length between two cows is 9-1 == 8, but we have 3 cows. to find the disctance between 2 cows 
# we need to find mid which will give us number of distance between 2 cows. if the distance is not exceeding the array limit 
# then the mid is True we can move higher side to find out the largest minimum distance.

def isValid(arr, mid, cow):
    c = 1 
    lastposition = arr[0]
    # [1,2,4,8,9]
    for i in range(1,len(arr)):
        if (arr[i] - lastposition)>= mid:
            lastposition = arr[i]
            c += 1
        
        if (c == cow): return True 

    return False

def AggresiveCow(arr, cow):
    start = min(arr)
    end = max(arr) - min(arr)
    ans = 0
    SortedArr = sorted(arr)
    while start <= end:
        mid = start + (end - start) //2
        if isValid(SortedArr, mid, cow ):
            ans = mid 
            start = mid + 1
        else:
            end = mid - 1
            
    return ans

if __name__ == '__main__':
    arr = [1,2,8,4,9]
    cow = 3
    res = AggresiveCow(arr, cow)
    print(res)