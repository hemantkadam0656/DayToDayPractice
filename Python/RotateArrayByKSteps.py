# Que:- Rotate an array right by k steps?

# Steps:
# check the length of array, if it is len that 2 then return None 
# Reverse the array first then iterate through the len(array)-1-k 
# Exchange the values by using two pointer method 


def  RotatedArray(arr, k):
    n = len(arr)
    k = k % n
    rev_arr = arr[::-1]

    x = 0 
    y = k - 1 
    while x <= y:
        rev_arr[x], rev_arr[y] = rev_arr[y], rev_arr[x]
        x += 1
        y -= 1

    i = k # 3
    j = n-1     # 4
    while i <= j:
        rev_arr[i], rev_arr[j] = rev_arr[j], rev_arr[i]
        i += 1
        j-= 1
    
    return rev_arr


# method 2 
# rotate the array without using extra space 

def RotateArrayInPlace(arr, k):
    n = len(arr)
    i = 0 
    j = n-1

    while i<=j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
    x = 0
    y = k-1 
    while  x <= y:
        arr[x], arr[y] = arr[y], arr[x]
        x += 1
        y -= 1

    a = k 
    b = n-1
    while a <= b:
        arr[a], arr[b] = arr[b], arr[a]
        a += 1
        b -= 1
    
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 2
    res = RotatedArray(arr, k)
    result = RotateArrayInPlace(arr, k)

    print(result)
