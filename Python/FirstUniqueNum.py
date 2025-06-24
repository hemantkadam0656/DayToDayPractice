firstList = [2,1,4,6,3]
SecList = [1,7,8,3,2]


# return the pair of the indices of number matching in both list 
# {1:(1,0), 2:(0,4), 3:(4,3)}


dict1 = {key:value for key, value in enumerate(firstList)}

dict2 = {key:value for key, value in enumerate(SecList)}

# print(dict1, dict2 , end=" ")

# resdict = {value1 : (key1, )  for key1, value1 in dict1.items() if value1 in dict2.values()}

# print(resdict)