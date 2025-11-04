def SelectionSorting(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == '__main__':
    arr = [64, 34, 25, 5, 22, 11, 90, 12]
    res = SelectionSorting(arr)
    print(res)


