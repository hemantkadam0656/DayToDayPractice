def BinaryToDecimal(Num):
    tot = 0
    pow = 1
    while Num > 0:
        rem = Num % 10 
        tot += rem * pow
        Num = Num // 10
        pow *= 2
    
    return tot

if __name__ == '__main__':
    Num = 100010011
    result = BinaryToDecimal(Num)
    print(result)




