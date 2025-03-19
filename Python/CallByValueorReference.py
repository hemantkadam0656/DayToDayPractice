# Python code to demonstrate
# call by reference

def add_more(list):
	list = [10, 20, 30, 40, 50]
	print("Inside Function", list)

# Driver's code
mylist = [10, 20, 30, 40]

add_more(mylist)
print("Outside Function:", mylist)




# # Python code to demonstrate
# # call by value
# string = "Geeks"

# def test(string):
# 	string = "GeeksforGeeks"
# 	print("Inside Function:", string)

# # Driver's code

# print("Outside Function:", string)
# test(string)