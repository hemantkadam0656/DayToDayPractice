# Amstrong number is nothing but a number is equal to the summasion of cube of their digits. 
# ex:- 371 == 3**3 + 7**3 + 1**3

def AmstrongNum(n):
    sum = 0 

    while n != 0 :
        rem = n % 10 
        sum = sum + rem**3
        print(sum)
        n //= 10 

    return sum 

if __name__ == '__main__':
    num = 371
    res = AmstrongNum(num)
    print(res)


