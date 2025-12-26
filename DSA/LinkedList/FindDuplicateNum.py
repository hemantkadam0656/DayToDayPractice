# To find the duplicate number, we are using linked list pattern which indicates index as node and value (or elements of arr) as next node.
# Why we are using linked list, because it has algorithm name floyd's algorithm and Hare algorithm which helps us to find cycle in array. 
# 0 → 1 → 3 → 2  →  4
#             ↑     ↓
#             └─────┘
# Here we are using slow and fast method which helps us to find cycle into the array. 
# Algorithm: - 
# 1. Assign first ele of arr to both variables ( slow and fast)
# 2. increment slow with 1 and fast with 2 untill slow == fast
# 3. Once you find duplicate value then assign assign first value again into slow and increment fast by 1. 
# 4. The place or index where slow and fast meet's that number is duplicate number 
# 

def DuplicateNum(arr):
    n = len(arr)
    slow = 0
    fast = 0

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    slow = 0 
    while (slow != fast):
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

if __name__ == '__main__':
    arr = [1, 3, 4, 2, 2]
    res = DuplicateNum(arr)
    print(res)
