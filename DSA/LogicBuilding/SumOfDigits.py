#sum of digits 145 

def SumOfDigits(num):
    total  = 0
    while num > 0:
        rem = num % 10 
        total += rem 
        num = num // 10 
    return total


if __name__ == '__main__':
    number = 123456
    res= SumOfDigits(number)
    print('The total of your given number is :', res)