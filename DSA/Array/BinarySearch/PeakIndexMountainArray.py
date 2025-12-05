# To find index of element at peak postion 
# we can use Binary Search
# here we are starting with start = 1 and end = len(arr)-2, because of the condition (arr[mid -1] < arr[mid] > arr[mid + 1]). 
# This condition will fail, if we start from 0  and end = len(arr)-1. why it will fail, because of suppose our mid is at end or start in 
# that case our (arr[mid -1] < arr[mid] > arr[mid + 1]) will fail. means we will error message saying Indexerror
#  

def PeakIndexMountainArray(arr):
    start = 1
    end = len(arr)-2

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid-1] < arr[mid]  and arr[mid] > arr[mid+1]:
            return arr[mid] 
        
        if arr[mid-1] < arr[mid]:
            start = mid+1
        else:
            end = mid-1 


if __name__ == '__main__':
    arr = [3,4,5,6,7,8,9,1,2]
    
    res = PeakIndexMountainArray(arr)
    print(res)





# arr2 = [8,9,0,1,2,3,4,5,6,7]