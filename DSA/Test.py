


def countPrimes( n: int) -> int:
    isPrime = [True] * (n+1) 
    if n == 0 or n== 1:
        return 0 
        
    isPrime[0] = False
    isPrime[1] = False 

    i = 2
    print(isPrime)
    while i*i <= n :
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = False 
        i+=1 
    
    
    print(isPrime)
    count = 0 
    for i in range(2, n+1):
        if isPrime[i]:
            count += 1
    
    return count
    


if __name__ == "__main__":
    number = 10
    res = countPrimes(number)
    print(res)

