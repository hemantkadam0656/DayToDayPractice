def ContainDuplicate(nums, k):
    ind = {}

    for i in range(len(nums)):
        if nums[i] in ind.keys():
            if abs(ind[nums[i]] - i) <= k:
                return True
        
        ind[nums[i]] = ind.get(nums[i], 0) + i
        print(ind)

    return False

if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    res = ContainDuplicate(nums, k)
    print(res)