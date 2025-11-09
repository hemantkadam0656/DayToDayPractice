def partition(arr, low, high):
    pivot = arr[high]
    i = low-1 

    for j in range(low, high):
        if arr[j] < arr[high]:
            




def quickSort(arr, low = 0, high= None):
    
    if high is None:
        high = len(arr)-1

    while low <= high:
        pivot_inedx = partition(arr, low, high)
    pass
    

if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    res = quickSort(arr, 0, len(arr) -1 )


