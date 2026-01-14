# Question:- Find the second largest element in an array without sorting?

# steps:
# check length of arr if it is less than 2 then return None
# Assign -inf value to both largest and second largest element variables
# Iterate throgth array and check the current element if greater than the latgest value 
# if yes then assign the values into largets variable otherwise check if the current values 
# if smaller than largest value and greater than the second largest value
# if yes then assign into the second largets value variable and return 
# if all element are same then return None 

def SecondLargestElement(arr):
    n = len(arr)

    if len(arr) < 2:
        return None
    
    largest = sec_largest = float('-inf')

    for num in arr:
        if num > largest:
            sec_largest = largest
            largest = num 
        elif largest > num > sec_largest:
            sec_largest = num 

    if sec_largest == float('-inf'):
        return None
   
    return sec_largest

if __name__ == '__main__':
    arr = [10, 5, 20, 8, 9, 1, 4]
    res = SecondLargestElement(arr)
    print(res)