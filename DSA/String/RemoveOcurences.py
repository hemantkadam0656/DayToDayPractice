# To remove the ocurence of substring from the string, we can use built-in replace function. 

def RemoveAllOcurences(string, substr):
    n = len(string)
    m = len(substr)
    i = 0 

    while i <= n:
        re = string.replace(substr, "")
        string = re
        i += 1

    print(re)

def WithoutBuiltInMethod(string, substr):
    n = len(string)
    m = len(substr)
    i = 0 
    j = 0 
    first = 0 
    sec = 0 
    end = 0
    NewString = string

    while i<= n :
        # NewString = 'daabcbaabcbc'
        # substr = 'ab'

        if NewString[i] == substr[j]:
           
            if end == m-1:
                NewString += string[:first] + string[sec:]

# To solve this question without using built-in function, I suppose to use sliding window algorithm. 
# keeping problem unsolved to understand the sliding window algorithm.  
        


if __name__ == '__main__':
    string = 'daabcbaabcbc'
    substr = 'ab'
    res = RemoveAllOcurences(string, substr)
    wt = WithoutBuiltInMethod(string, substr)