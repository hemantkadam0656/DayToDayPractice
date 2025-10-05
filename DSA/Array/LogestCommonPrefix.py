def longestCommonPrefix(arr):
    minLen = min(arr, key=len)
    n = len(arr)
    i = 0 
    letterList = []
    print(n)
    
    while i < len(minLen):
        letter = arr[0][i]
        # print(arr[0][i])
        for j in range(1,n): 
            if arr[j][i] == letter:
                # print(arr[j][i])
                letterList.append(arr[j][i])
        
        i += 1

    print(letterList)  

strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
 