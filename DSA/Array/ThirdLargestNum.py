# This method is useful for array containing distict numbers / sorting method

def SimpleMethodforThirdLargest(arr):
    n = len(arr)
    i = 0 

    while i < n:
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        
        i += 1

    return arr[n - 3]
    
def ThreeLoopMethod(arr):
    n = len(arr)

    first = float('-inf')
    for i in range(n):
        if arr[i] > first:
            first = arr[i]

    second = float('-inf')
    for j in range(n):
        if arr[j] > second and arr[j] < first:
            second = arr[j]
    
    third = float('-inf')
    for k in range(n):
        if arr[k] > third and arr[k] < second:
            third = arr[k]
    
    return third


def SingleLoopThirdLargest(arr):
    n = len(arr)
    first, second, third = float('-inf'), float('-inf'),float('-inf')

    for i in range(n):
        if arr[i] > first:
            third = second
            second = first 
            first = arr[i]

        elif arr[i] > second:
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]

        else:
            continue
    
    return third

if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 8, 9]
    inst = SimpleMethodforThirdLargest(arr)
    inst2 = ThreeLoopMethod(arr)
    inst3 = SingleLoopThirdLargest(arr)
    print(inst)
    print(inst2)
    print(inst3)

    

