# Kadane's Alhorithm 

def FindMaxSubarraySum(arr):
    n = len(arr)
    currSum = 0 
    maxSum = float('-inf')

    for i in range(n):
        currSum += arr[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0 
            
    return maxSum

if __name__ == '__main__':
    arr = [-4,-5,1,-2,-7,-3,-9]
    res = FindMaxSubarraySum(arr) 
    print(res)




