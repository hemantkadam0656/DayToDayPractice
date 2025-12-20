def ReverseNumber(num):
    revNum = 0
    while num > 0:
        rem = num % 10 
        revNum = revNum * 10 + rem 
        num //= 10 


    return revNum



if __name__ == '__main__':
    num = 4537
    res =  ReverseNumber(num)
    print(res)



