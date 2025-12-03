# To find index of element at peak postion 
# we can use Binary Search


def PeakIndexMountainArray(arr):
    start = 1 
    end = len(arr)-2

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid -1] < arr[mid] > arr[mid + 1]:
            return mid 
        
        if arr[mid -1 ] < arr[mid]:
            start = mid+1
        else:
            end = mid-1 


         



if __name__ == '__main__':
    arr = [3,4,5,6,7,8,9,1,2]
    arr2 = [8,9,0,1,2,3,4,5,6,7]

    res = PeakIndexMountainArray(arr)

