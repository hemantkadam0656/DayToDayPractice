# explaination: - we have x as number and n as power to that number like 2^10, 
# now suppose need find binary numer of 10, so for that we can divide 10 by 2  ==  1010 = 2^3 + 2^2 + 2^1 + 2^0    
# 5 % 2 == 1  --> 1 * 2 == 2 __ x = 2*2 == 4
# 2 % 2 == 0  skip  --> 4 * 4 == 16 
# 1 % 2 == 1  --> 2 * 16 == 32 
# 0 % 2 == 0 break 

def MyPower(x, n):
    if (n == 1): return x
    if (n == 0): return 1
    if (x == 1): return 1
    if (x == 0): return 0
    if (x == -1 & n % 2 == 0): return 1
    if (x == -1 & n % 2 != 0): return -1  


    if (n < 0):
        n = -n 
        x = 1/ x
        
    ans = 1
    while n > 0 :
        if n % 2 == 1:
            ans *= x

        x *= x
        n //= 2 
    
    return ans  


if __name__ == '__main__':
    x = 2
    n = 5
    res = MyPower(x, n)
    print(res)




