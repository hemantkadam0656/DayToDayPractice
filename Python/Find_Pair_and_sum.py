list = [8, 7, 2, 5, 3, 1]
target = 10
 
dict = {}

lst = []

for i, num in enumerate(list):
    if num in dict:
        lst.append((dict[num], i))
    else:
        dict[target - num] = i
        
print(dict)
print(lst)