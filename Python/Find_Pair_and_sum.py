# list = [8, 7, 2, 5, 3, 1]
# target = 10
 
# dict = {}

# lst = []

# for i, num in enumerate(list):
#     if num in dict:
#         lst.append((dict[num], list[i]))
#     else:
#         dict[target - num] = list[i]
        

# print(lst).




# importing the multiprocessing module
import multiprocessing
import multiprocessing.process




var = 0
def cube(num):
    
    print(num**3)

def sqare(num):
    var = 3 
    
    print(num**2)


cube(2)
print(var)
sqare(1)
print(var)


# if __name__ == '__main__':

#     p1 = multiprocessing.Process(target= cube, args = (10,))
#     p2 = multiprocessing.Process(target= sqare, args = (10,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

