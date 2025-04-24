list = [4,6,7,8,1,2,5,2,32,76,12,76,9]

n = len(list)


for i in range(n):
    for j in range(i+1,n):
        if list[j] < list[i]:
            list[i], list[j] = list[j], list[i]
            
print(list)