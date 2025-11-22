def Factorial(n):
    tot = 1
    for i in range(1,n+1):
        tot = tot * i
            
    return tot

if __name__ == '__main__':
    num = 4
    R = 2
    fact_n = Factorial(num)
    fact_r = Factorial(R)
    fact_NmR = Factorial(num-R)

    result = fact_n // (fact_r * fact_NmR)

    print(result) 



