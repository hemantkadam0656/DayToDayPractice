# lst1 = [-1,1,-2,2,-3,3,-4,-5,-6]
# lst2 = [1,1,-2,2,-3,3,-4,-5,-6]

# result = []

# for i,j in zip(lst1, lst2):
#     if i < 0 and j < 0 :
#         res = i * j 
#         result.append(res)

# print(result)

# def decorator(fun):
#     def wrapper():
#         print('before fiunction calls')
#         fun()
#         print('after function calls')

#     return wrapper




# @decorator
# def hello():
#     print('Hello World')

# hello()


# list = [1,2,3,4,5,6,7,8]


# newlist = iter(list)

# print(next(newlist))
# print(next(newlist))
# print(next(newlist))
# print(next(newlist))





# target = 10

# dict = {}

# lst1 = []

# for i, num in enumerate(list):
#     if num in dict:
#         lst1.append((dict[num], list[i]))
#     else:
#         dict[target - num] = list[i]
    

# print(lst1)

# import copy

# my_list = [8, 7, 2, 5, 3, 1]

# y = copy.copy(my_list)

# y.append(99)

# print(y)
# print(my_list)


# class Metaclass:
#     pass 


# obj = Metaclass

# print(type(Metaclass))


# bank = type('BankAccount', (), {'x':10})

# obj = bank

# from functools import reduce

# my_list = [1,2,3,4,5]

# def my_fun(x,y):
#     print(x,y)
#     return x - y 


# obj = reduce(my_fun,my_list)

# print(obj)

# import re

# s = 'There are lots of associate in tcs those are want to move on-site'

# ns = re.subn('are', 'of', s)

# print(ns)


# dict1 = {1: 1, 2:2, 3:3}

# dict2 = {1:3, 2:2, 3:1}

# newdict = {x : (lambda y: y * y)(y) for x, y in dict1.items() if x in dict2.keys()}

# print(newdict)


# import re 


# fullname = 'Hemant Pundlik Kadam'


# regex = r"([a-zA-Z]+) (\d+)"



# match = re.match(regex, fullname)

# if match:
#     print(match)
# else:
#     print("no match")


# import re
# password = 'Hema@gmail.com  kadam '

# mail = re.findall('\S+@\S+', password)


# print(mail)

 




# def solution(A):
#     N = len(A)      # number of hospitals
#     M = len(A[0])   # number of days

#     repeated_doctors = []  # stores unique doctors who worked in >1 hospital on same day

#     for day in range(M):
#         doctor_ids = []         # doctor IDs seen on this day
#         doctor_duplicates = []  # doctors who are duplicated on this day

#         for hospital in range(N):
#             doc_id = A[hospital][day]

#             # check if already seen
#             found = False
#             for d in doctor_ids:
#                 if d == doc_id:
#                     found = True
#                     break

#             if found:
#                 # check if already added to duplicates
#                 already_dup = False
#                 for d in doctor_duplicates:
#                     if d == doc_id:
#                         already_dup = True
#                         break
#                 if not already_dup:
#                     doctor_duplicates.append(doc_id)
#             else:
#                 doctor_ids.append(doc_id)

#         # now add these duplicates to global result if not already added
#         for doc in doctor_duplicates:
#             already_global = False
#             for g in repeated_doctors:
#                 if g == doc:
#                     already_global = True
#                     break
#             if not already_global:
#                 repeated_doctors.append(doc)

#     return len(repeated_doctors)



# print(solution([[1, 2, 2], [3, 1, 4]]))  # ➞ 1
# print(solution([[1, 1, 5, 2, 3], [4, 5, 6, 4, 3], [9, 4, 4, 1, 5]]))  # ➞ 4
# print(solution([[4, 3], [5, 5], [6, 2]]))  # ➞ 0
        # M
# A = 1   2    2
# N   3   1    4




# import copy  

# a = [[1, 2, 3], [4, 5, 6]]

# # Creating a shallow copy of the nested list 'original'
# b = copy.copy(a)

# # Modifying an element in the shallow-copied list
# b[0][0] = 99

# # Printing the original and shallow-copied lists  
# print(b)
# print(a)



# import copy

# a = [[1, 2, 3], [4, 5, 6]]

# # Creating a deep copy of the nested list 'a'
# b = copy.deepcopy(a)

# # Modifying an element in the deep-copied list


# b[0][0] = 99 
# print(b)
# print(a)


# s = 'AABCAAADA'
# k = 4

# n = len(s)/k
# mylist = [s[i:i+k] for i in range(0, len(s), k)]

# chars = [list(i) for i in mylist]
# for lst in chars:
#     unique = []
#     for char in lst:
#         if char not in unique:
#             unique.append(char)
    
#     word = ''.join(unique)
#     print(word)

        
# print()

def count_ones_and_positions(n):
    binary = []
    
    while n > 0:
        binary.append(n % 2)
        n //= 2

    binary = binary[::-1]

    positions = []
    position = 1  
    found_first_one = False

    for bit in binary:
        if bit == 1:
            positions.append(position)
            found_first_one = True
        if found_first_one:
            position += 1

    print(len(positions))  
    print(*positions)     

count_ones_and_positions(161)