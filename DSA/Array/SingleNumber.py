def FindSingleNum(arr):
    dict = {}
    for i, num in enumerate(arr):
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for key, value in dict.items():
        if value == 1:
            return key
        
    return -1 

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,5,3,2,1,6,4]
    res = FindSingleNum(arr)
    print(res)


# Another way to find out the single number is a bitwise XOR opertor 

def bitwiseOpt(mylist):
    const = 0 
    for i in mylist:
        const ^= i

    return const


if __name__ == '__main__':
    mylist = [1,2,3,4,5,6,5,3,2,1,4]
    result = bitwiseOpt(mylist)
    print(result)




