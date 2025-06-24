str = 'madam'
flag = False 

if len(str) == 0 | len(str) == 1:
    print(-1)
else:
    newastr = str[::-1]
    
    for i in range(len(str)):
        if str[i] == newastr[i]:
            flag = True
        else:
            flag = False 
    

print(flag)
        
