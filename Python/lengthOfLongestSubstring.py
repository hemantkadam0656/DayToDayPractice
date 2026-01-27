def lengthOfLongestSubstring(s):
    char_ind = {}
    left = 0 
    max_len = 0 

    for i in range(len(s)):

        if s[i] in char_ind and char_ind[s[i]] >= left:
            left = char_ind[s[i]] + 1

        char_ind[s[i]] = i
        print(char_ind)
        max_len = max(max_len, i - left + 1 ) 
    
    return max_len

if __name__ == '__main__':
    s = "bbbb"
    res = lengthOfLongestSubstring(s)
    print(res)

