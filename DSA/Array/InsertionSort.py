def InsertionSort(arr):
    n = len(arr)

    for i in range(n):
        curr = arr[i]
        j = i-1

        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = curr

    return arr

if __name__ == '__main__':
    arr = [5,4,1,6,2,3]
    res = InsertionSort(arr)
    print(arr)


