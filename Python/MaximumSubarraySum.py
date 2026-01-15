def MaximumSubArraySum(nums):
    n = len(nums)
    curr_sum = nums[0]
    max_sum = nums[0]
   
    for i in range(n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

if __name__ == '__main__':
    nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
    res = MaximumSubArraySum(nums)
    print(res)


