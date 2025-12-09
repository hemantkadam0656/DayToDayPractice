def InsertionSort(arr):
    n = len(arr)

    for i in range(n):
        smallestIdx = i 
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                smallestIdx = j 
        
        arr[smallestIdx],arr[j] = arr[j],arr[smallestIdx]
       

    return arr

if __name__ == '__main__':
    arr = [4,5,1,6,2,3]
    # i = 0 == [1,5,4,6,2,3]
    # i = 1 == [1,2,4,6,5,3]
    # i = 2 == [1,2,3,6,5,4]
    # i = 3 == [1,2,3,4,5,6]
    # i = 4 == [1,2,3,4,5,6]
    res = InsertionSort(arr)
    print(arr)


