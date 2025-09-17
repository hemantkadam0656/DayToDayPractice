def binary_Search(nums, x):
    low = 0
    high = len(nums) - 1 

    while low <= high:
        mid = low + (high - low) // 2 # 0 + 5 // 2 = 2

        if nums[mid] == x:
            return mid

        elif  x > nums[mid]:
            low = mid + 1 
        
        else:
            high = mid - 1

    return -1  


if __name__ == '__main__':
    nums = [-1, 2, 3, 4, 10, 40]
    x = -1 
    res = binary_Search(nums, x)
    print(res)
