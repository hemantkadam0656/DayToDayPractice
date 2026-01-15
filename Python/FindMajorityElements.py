def MajorityElements(nums):
    n = len(nums)
    count = {}

    for i in range(n):
        if nums[i] in count.keys():
            count[nums[i]] = count.get(nums[i], 0) + 1
        else:
            count[nums[i]] = 1
    
    max_ele = max(count.items(), key = lambda item : item[1])

    return max_ele[0]

# Best Approch is to use boyes-moore voting algorithm 

def BoysMooreAlgorithm(nums):
    candidate = nums[0]
    count = 0 

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num== candidate else -1 

    return candidate


if __name__ == '__main__':
    nums = [2,2,1,1,2,2,2]
    res = MajorityElements(nums)
    omendvar = BoysMooreAlgorithm(nums)
    print(res)
    print(omendvar)