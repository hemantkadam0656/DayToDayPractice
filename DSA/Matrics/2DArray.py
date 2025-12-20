# Finding element in 2D array which is having 4 rows and 3 columns

def TwoDArray(arr, target):
    row = len(arr)
    column = len(arr[0])

    for i in range(row):
        for j in range(column):
            if arr[i][j] == target:
             print(arr[i][j], end=" ")
             print()
             print(i,j)
    
    return (-1,-1)


# find the maximum row sum from 2D array 
def MaximunRowSum(arr):
    maxSum = float('-inf')
    row = len(arr)
    col = len(arr[0])
    sum = 0

    for i in range(row):
        for j in range(col):
            sum += arr[i][j]

        maxSum = max(maxSum, sum)
        sum = 0 

    return maxSum

# Find maximum sum of column from 2d array 

def MaximumColSum(arr):
    maxColSum = float('-inf')
    row = len(arr)
    col = len(arr[0])
    sum = 0 

    for i in range(col):
        for j in range(row):
            sum += arr[j][i]

        maxColSum = max(maxColSum, sum) 
        sum = 0 
    
    return maxColSum
 

# Find the digonal Sum of 2D array 
# Note:- There are two digonals are avaiable in matrix Primary digonal and secondary digonal

def DigonalSum(array):
    PD_sum = 0
    SD_sum = 0
    sum = 0
    n = len(array)
    row = len(array)
    col = len(array[0])

    for i in range(row):
        for j in range(col):
            print(array[i][j], end=" ")
        print()

    # Primary digonal
    # for i in range(row):
    #     PD_sum += array[i][i]

    # print(PD_sum)
    
    # for i in range(row):
    #     SD_sum += array[i][row-i-1]
    
    # print(SD_sum)

    for i in range(n):
        for j in range(n):
            if (i == j):
                sum += array[i][j]
            elif( j == n-i-1):
                sum += array[i][j]


    return sum 
  

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    array = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
    target = 14
    # res = TwoDArray(arr, target)
    # print(res)

    # tot_row_sum = MaximunRowSum(arr)
    # print(tot_row_sum)

    # tot_col_sum =  MaximumColSum(arr)
    # print(tot_col_sum)

    Digonal_Sum = DigonalSum(array)
    print(Digonal_Sum)


   











