# To find count or prime numbers for till given number, we gonna use sieve eratostenes algorithm
# In this algo first we need to consider all the numbers till given number as prime number.
# Then start the loop number 2 (because 0 and 1 is not prime numebrs) then remove the number multiple of 2 and continue in loop.
# 


def PrimeNum(num):
    arr = [True] * (num + 1)

    arr[0] = False
    arr[1] = False

    i = 2
    while i*i <= num:
        if arr[i]:
            for j in range(i*i, num +1, i):
                arr[j] = False

        i += 1
    
    primes = []
    for i in range(2, num+1):
        if arr[i]:
            primes.append(i)
    
    return primes


if __name__ == "__main__":
    number = 50
    res = PrimeNum(number)
    print(res)