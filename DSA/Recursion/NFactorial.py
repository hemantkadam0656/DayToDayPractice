def Nfactorial(n):
    if n == 0:
        return 0
    
    return n + Nfactorial(n-1)

if __name__ == '__main__':
    n = 5
    res = Nfactorial(n)
    print(res)