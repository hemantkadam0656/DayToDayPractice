def FindMissingNum(nums):
    n = len(nums)
    actual_sum  = 0
    expected_sum = sum(nums)

    actual_sum = n * (n+1) // 2
    missing_num = actual_sum - expected_sum
    return missing_num


def UsingXor(nums):
    xor = 0 
    n = len(nums)

    for i in range(n):
        xor ^= i 
        xor ^= nums[i]

    xor ^= n 
    return xor 
		

if __name__ == '__main__':
    nums = [3, 0, 1]
    res = FindMissingNum(nums)
    result = UsingXor(nums)
    print(res)
    print(result)