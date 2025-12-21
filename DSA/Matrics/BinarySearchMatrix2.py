# Typical Search Approach (Reminder)
# Start from top-right corner:
# If target is smaller → move left
# If target is larger → move down

def BinarySearchMatrixII(arr, target):
    m = len(arr)
    n = len(arr[0]) # 5
    
    row = 0
    col = n-1 

    while (row < m and col >= 0):
        if target == arr[row][col]:
            return (row, col)
        elif target < arr[row][col]:
            col -= 1
        else:
            row += 1

    return (-1,-1)    

if __name__ == '__main__':
    arr = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    target = 30
    
    res = BinarySearchMatrixII(arr, target)
    print(res)


