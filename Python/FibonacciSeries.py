def fabonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)
    
n = 6
for i in range(0,n):
    print(fabonacci(i), end=" ")