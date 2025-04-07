def Pyramid(n):
    for i in range(n):
        print((' '* (n-i)) + ('*' * (i + 1)) + ('*' * i)  )


n = 5

Pyramid(n)
