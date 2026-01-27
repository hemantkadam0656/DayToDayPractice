
# 0, 1, 1, 2, 3, 5, 8......

def FibonnaciSeries(arr, n):
    if n == 0 or n == 1:
        return  True
    print(arr[n-2])
    return arr[n-1] >= arr[n-2] and FibonnaciSeries(arr, n-1)


if __name__ == '__main__':
    arr = [1,2,8,4,5]
    n = 5
    res = FibonnaciSeries(arr, n)
    print(res)

