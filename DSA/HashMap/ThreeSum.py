
def ThreeSumBF(arr):
    n = len(arr)
    list = []

    # BruteForce Method 
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    list.append((i,j,k))
    
    return list 



def ThreeSumHashing(arr):

    # here we are using simple math techniq, which say's  if a+b+c == 0 --> b+c = -a --> c = -(a+b)
    # we gonna use Hashing techniq to solve the below problem. 

    n = len(arr)
    result = set()

    for i in range(n):
        seen = set()
        target = -arr[i]

        for j in range(i + 1, n):
            third = target - arr[j]

            if third in seen:
                triplet = tuple(sorted((arr[i], arr[j], third)))
                result.add(triplet)

            seen.add(arr[j])

    return [list(t) for t in result]
 

def TwoPointerMethod(arr):
    n = len(arr)
    sum = 0 
    arr = sorted(arr)

    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            sum = arr[i] + arr[j] + arr[k] 
            if sum == target:
                return (arr[i], arr[j], arr[k])
            elif sum > target:
                k -= 1
            else:
                j += 1

    return -1 

if __name__ == "__main__":
    arr = [-1,0,1,2,-1,-4]
    target = 3
    res = ThreeSumBF(arr)
    ans = ThreeSumHashing(arr)
    result = TwoPointerMethod(arr)
    print(result)


