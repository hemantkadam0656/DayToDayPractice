num = 6

n1, n2 = 0, 1
i = 0

if num == 0:
    print(0)
elif num == 1:
    print(1)
else:
    while i < num:
        print(n1)
        n = n1 + n2 
        n1 = n2 
        n2 = n
        i +=1



    