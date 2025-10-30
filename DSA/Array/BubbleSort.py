
def BubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr 


def optimizedBubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == '__main__': 
    arr = [7, 3, 9, 12, 11]
    res = BubbleSort(arr)
    res2 = optimizedBubbleSort(arr)
    print('first :-', res)
    print(res2)