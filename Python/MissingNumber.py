def MissingNumber(nums):
    n = len(nums)
    i = 1
    while i < n:
        if i in nums:
            i+= 1        
    
    return i 

if __name__ == '__main__':
    nums = [2,1,3,3,4]
    res = MissingNumber(nums)
    print(res)