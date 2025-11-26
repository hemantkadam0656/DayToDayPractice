def MaxSubarraySum(arr):
    n = len(arr)
    maxSum = 0 
    for i in range(n):
        currSum = 0
        for j in range(i,n):
            currSum += arr[j]
            maxSum = max(maxSum, currSum)
        
    return maxSum


if __name__ == '__main__':
    arr = [1,2,-3,4,-5,6,7,8]
    res = MaxSubarraySum(arr)
    print(res)