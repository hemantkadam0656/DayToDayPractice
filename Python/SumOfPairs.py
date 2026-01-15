def TwoSum(nums, target):
    pair = {}

    for key, value in enumerate(nums):
        sec = target - value

        if sec in pair.keys():
            return (key, pair[sec])
        else:
            pair[value] = key 


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = TwoSum(nums, target)
    print(res)