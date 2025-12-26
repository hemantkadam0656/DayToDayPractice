def fun(arr):
    n = len(arr)
    i = 0
    cost = 0

    while n > 1 :
        minVal = min(arr[i-1], arr[i+1])
        cost += minVal 
        arr[i] = max(arr[i], minVal)
        n -= 1

    return cost


if __name__ == "__main__":
    arr = [1,1,3,2,4]
    res = fun(arr) 
    print(res)