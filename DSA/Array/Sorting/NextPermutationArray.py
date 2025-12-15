
# find the lexicological array (next permutation array) 
# Steps:- 
# 1. Find the pivot index 
# 2. swap the right most smaller number with pivot index element 
# 3. swap the remaining elements from pivot+1 to n-1 
# 4. check the pivot index is still -1, if yes then reverse the array 


def NextPermutationArray(arr):
    # print(arr)
    n = len(arr)
    pivot = -1 

    for i in range(n-2, -1, -1):
        #        [1,2,5,4,3]
        #  idx = [0,1,2,3,4]
        if arr[i] < arr[i+1]:
            pivot = i
            break
       
    if pivot == -1:
        arr = [arr[i] for i in range(n-1, -1, -1) ]
        return arr
    
    for i in range(n-1, pivot, -1 ):
        #        [1,2,5,4,3]
        #  pivot = 1 
        #  idx = [0,1,2,3,4]
        if arr[i] > arr[pivot]:
            arr[pivot], arr[i] = arr[i], arr[pivot]
            break
    
    #[1,3,5,4,2] 
    i = pivot + 1
    j = n-1 
    while i <= j :
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
    return arr

if __name__ == '__main__':
    num = 54321
    arr = [int(i) for i in str(num)]
    res = NextPermutationArray(arr)
    print(res)

