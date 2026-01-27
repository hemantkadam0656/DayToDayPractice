def RecursionI(n):
    if n < 1:
        return 
    
    print(n, end=" ")
    RecursionI(n-1)


if __name__ == '__main__':
    n = 100 
    res = RecursionI(n)
    # print(res)
    