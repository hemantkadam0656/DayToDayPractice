list = [2,7,11,15] 

target = 9

dict = {}

for i, num in enumerate(list):
    if num in dict:
        print(dict[num], i)
    else:
        dict[target - num] = i


print(dict)