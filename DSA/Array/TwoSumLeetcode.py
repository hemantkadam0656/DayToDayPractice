
def twoSum(nums, target: int):
    n = len(nums)
    resDict = {}
    resList = []
    for key, value in enumerate(nums):
        res = target - value 
        if value in resDict:
            return [resDict[value], key]
        else:
            resDict[res] = key 
    
    return resList


if __name__ == '__main__':
    nums = [2,7,11,15] 
    target = 9  
    res = twoSum(nums, target)