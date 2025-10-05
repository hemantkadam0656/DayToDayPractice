# Horizontal Scanning pattern method

def LogestCommonPrefix(arr):
    prefix = arr[0]

    for s in arr[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix



arr = ["flower","flow","flight"]
res = LogestCommonPrefix(arr)
print(res)

