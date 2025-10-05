def LogestCommonPrefix(arr):
    minLen = min(arr, key= len)

    for i in range(len(minLen)):
        ch = minLen[i]
        for s in arr:
            if s[i] != ch:
                return s[:i]
    
    return minLen

arr = ["flower","flow","flight"]
res = LogestCommonPrefix(arr)
print(res)

