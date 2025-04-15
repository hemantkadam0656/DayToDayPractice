list = [8, 7, 2, 5, 3, 1]
target = 10
 
dict = {}

for i, num in enumerate(list):
    if num in dict:
        print(dict[num], i)
    else:
        dict[target - num] = i
        
