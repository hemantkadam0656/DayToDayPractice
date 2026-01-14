# Find the subarray sum equal to K 

# Here we used brute force method which is required O(n*2) time complexity
def SubArraySum(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        sum = 0 

        for j in range(i,n):
            sum += arr[j]

            if sum == target:
                count+=1
        
    return count

# Here we are using optimal approch called prefix Sum array,  which take time complexity as O(n) and space complexity O(n) 
# steps: - 
# create one array(prefix) to get sum of all element till the ith position of array into it.
# apply loop  


def PrefixSum(arr):
    n = len(arr)
    preFix = [0]*(n)
    sum = 0
    hashmap = {}

    for i in range(n):
        sum += arr[i]
        preFix[i] = sum

    print(preFix)
    # preFix = [9, 13, 33, 36, 46, 51]
    # arr = [9,  4, 20,  3, 10,  5]
   
    i = 0
    j = 1
    while (i<j):
        sub = target - arr[j]
        # sub = 33 - 9 == 24 
        # sub = 33 - 4 == 29 
        # sub = 33 - 20 == 13 
        if preFix[i] == target:
            count += 1
        elif sub in hashmap:
            count += 

    







if __name__ == '__main__':
    arr = [9,4,20,3,10,5]
    target = 33
    res = PrefixSum(arr)
    print(res)

