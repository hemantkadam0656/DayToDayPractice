def MergeSortedArray(arr, nums):
    i = 2
    j = 4
    k = i + j + 1 
    while i >= 0 and j >= 0:
        if arr[i] > nums[j]:
            arr[k] = arr[i]
            i -= 1
        else:
            arr[k] = nums[j]
            j -= 1
        k -= 1

    # Copy remaining elements of nums (if any)
    while j >= 0:
        arr[k] = nums[j]
        j -= 1
        k -= 1

    return arr

if __name__ == '__main__':
    arr = [1,3,4,0,0,0,0,0]
    nums = [2,5,6,7,8]
    tot = arr + nums 
    print(tot)
    res = MergeSortedArray(arr, nums)
    print(res)

