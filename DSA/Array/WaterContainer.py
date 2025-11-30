# Brute Force Method

def WaterContainer(arr):
    MaxWater = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            currWater = min(arr[i], arr[j]) * (j - i)
            MaxWater = max(MaxWater, currWater)
            
    return MaxWater 


if __name__ == '__main__':
    heights = [1,8,6,2,5,4,8,3,7]
    MaxWater = WaterContainer(heights)
    print(MaxWater)

# -------------------------------------------------------------

# Best approch to solve this question and optimized techniq is Two Pointer method

def TwoPointer(arr):
    n = len(arr)
    fp = 0
    rp = n-1
    Water = 0

    while(fp < rp): 
        currLevel = min(arr[fp], arr[rp]) * (rp - fp)
        Water = max(Water, currLevel)

        if arr[fp] < arr[rp]:
            fp += 1
        else:
            rp -= 1
    
    return Water



if __name__ == '__main__':
    arr = [1,8,6,2,5,4,8,3,7]
    result = TwoPointer(arr)
    print(result)












