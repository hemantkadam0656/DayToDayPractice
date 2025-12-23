
def  TwoSum(arr, trg):
    n = len(arr)
    result = {}

    for key, value in enumerate(arr):
        second =  target - value
        if second in result.keys():
            return (key, result[second])
        else:
            result[value] = key

    return (-1,-1)  


if __name__ == '__main__':
    arr = [5,2,11,7,15]
    target = 25
    res = TwoSum(arr, target)
    print(res)