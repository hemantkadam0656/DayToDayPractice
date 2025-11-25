def Subarrays(arr):
    n = len(arr)
    resList = []
    for i in range(n):
        for j in range(i,n):
            resList.append(arr[i:j+1])

    return resList


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    res = Subarrays(arr)
    print(res)






