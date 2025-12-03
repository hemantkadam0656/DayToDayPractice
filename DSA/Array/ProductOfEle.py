# Que :- find out the product of array elements except self. 

# Brute Force method
def ProductOfElements(arr):
    n = len(arr)
    ProdList = []

    for i in range(n):
        prod = 1
        for j in range(n):
            if j != i:
                prod = prod * arr[j]

        ProdList.append(prod)
    
    return ProdList
            


if __name__ == '__main__':
    arr = [1,2,3,4]
    result = ProductOfElements(arr)
    print(result)


# Optimizing time complexity 

def OptimalWay(nums):
    n = len(nums)
    prefix = []
    suffix = []


    for i in range(n):
        prefix[i] = prefix[i-1] * nums[i-1]
        



if __name__ == '__main__':
    nums = [1,2,3,4]
    res = OptimalWay(nums)
    





