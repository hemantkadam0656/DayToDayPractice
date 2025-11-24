# Linear Search 

def LinearSearch(arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i]
        
    return -1 



if __name__ == '__main__':
    arr = [11, 12, 13, 14, 15]
    target = 20
    res = LinearSearch(arr)
    print('Target Number is :', res)

