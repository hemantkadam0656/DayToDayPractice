# Return the sorted array having squares of each number

def squareOfNums(nums):
    n = len(nums)
    squr = [0] * n 

    i = 0 
    j = n-1 
    pos = n-1

    while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            squr[pos] = nums[i] ** 2
            i += 1
        else:
            squr[pos] = nums[j] ** 2
            j -= 1

        pos -= 1

    return squr
   

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    res = squareOfNums(nums)
    print(res)