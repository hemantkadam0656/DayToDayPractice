n = 4

for i in range(n+1):
    if i == 0:
        print(' '* (n-i) + "*" )
    else:
        print(' ' *(n-i) + "*" + " "*(2*i-1) + '*' )
   
for j in range(n-1,-1,-1):
    if j == 0:
        print(' '* (n-j) + '*')
    else:
        print(' '* (n-j) + '*'+ ' '*(2*j-1)+'*')
    




