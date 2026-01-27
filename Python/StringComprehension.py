def StringComprehension(chars):
    n = len(chars)
    ele = 0
    cnt = 0 

    while cnt < n:
        char = chars[cnt]
        count = 0

        while cnt < n and chars[cnt] == char:
            cnt += 1 
            count += 1  
        
        chars[ele] = char 
        ele += 1

        if count > 1:
            for digit in str(count):
                chars[ele] = digit
                ele += 1
    
    return ele


if __name__ == '__main__':
    chars = ["a","a","b","b","c","c","c"]
    res = StringComprehension(chars)
    print(res)
