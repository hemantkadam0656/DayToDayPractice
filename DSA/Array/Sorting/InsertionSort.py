def InsertionSort(arr):
    n = len(arr)

    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        
        while  prev >= 0 and arr[prev] > curr:
            arr[prev + 1] = arr[prev]
            prev -= 1

        arr[prev + 1] = curr

if __name__ == '__main__':
    arr = [4,5,1,6,2,3]
   
    res = InsertionSort(arr)
    print(arr)


