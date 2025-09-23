# Finding Second largest number from given array

def SortingMethod(arr):
    # find second largest number by using sorting method
    i = 0
    n = len(arr)
    
    if n == 0 or n == 1:
        return -1 

    while i < n:
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        
        i += 1

    for i in range(n - 2, -1, -1):
        
        if arr[i] != arr[n -1]:
            return arr[i]
    
    return -1 


def TwoPassSearchMethod(arr):
    # Find the second Largest element by using two loops 
    n = len(arr)

    largest = -1 
    secondLargest = -1 

    for i in range(n):  # [12, 35, 1, 10, 34, 1]
        if arr[i] > largest:
            largest = arr[i]
        
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]

    return secondLargest


def OnePassSerchMethod(arr):
    # Find the Second largest number by using single loop
    n = len(arr)

    largest = -1 
    SecondLargest = -1 

    for i in range(n):

        if arr[i] > largest:
            SecondLargest = largest
            largest = arr[i]
        
        elif arr[i] < largest and arr[i] > SecondLargest:
            SecondLargest = arr[i]
  
    return SecondLargest


if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 1]
    res = SortingMethod(arr)
    print(res)
    res1 = TwoPassSearchMethod(arr)
    print(res1)
    res2 = OnePassSerchMethod(arr)
    print(res2)
    