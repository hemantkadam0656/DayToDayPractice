def  ValidPalindrome(s):
    ns = (''.join(char for char in s if char.isalnum())).lower()
    n = len(ns)
    print(ns)
    i = 0 
    j = n-1

    while i <= j: 
        if ns[i] == ns[j]:
            i += 1
            j -= 1
        else:
            return False 

    return True


if __name__ == '__main__':
    s = "A man a plan a canal Panama"
    res = ValidPalindrome(s)
    print(res)
