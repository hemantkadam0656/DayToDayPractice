def BinaryNum(num):
    digit = ''
    finalVal = ''
    while num > 0 :
       n = num % 2     
       digit += str(n)
       num = num // 2

    for i in range(len(digit)-1, -1 , -1 ):
        finalVal = finalVal + digit[i]
    return finalVal

if __name__ == '__main__':
    num = 50 
    res = BinaryNum(num)
    print('Binary Number for Given decimal number is :',res)


