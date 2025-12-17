def StringCompression(string):
    n = len(string)
    ch = ''
    count = 1

    for i in range(1,n):
        if string[i] == string[i-1]:
            count+=1
        else:
            ch = ch + string[i-1] + str(count)
            count = 1

    ch = ch + string[-1] 
    return ch 


if __name__ == '__main__':
    string = "aaabbccccd"
    res = StringCompression(string)
    print(res)