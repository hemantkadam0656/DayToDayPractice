def PairSum(arr, target):
    n = len(arr)
    firstNum = 0
    SecNum = n - 1

    for i in range(n):
        if arr[firstNum] + arr[SecNum] > target:
            SecNum -= 1
        elif arr[firstNum] + arr[SecNum] < target:
            firstNum += 1
        else:
            return (firstNum, SecNum)
    

if __name__ == '__main__':
    arr = [2,7,11,15,17,20]
    target = 19
    res = PairSum(arr, target)
    print(res)


