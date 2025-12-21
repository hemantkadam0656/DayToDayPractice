def SpriralMatrix(arr):
    rowstart = 0
    rowend = len(arr) - 1
    colstart = 0
    colend = len(arr[0]) - 1
    res = []


    while rowstart <= rowend and colstart <= colend:
        # Top row
        for i in range(colstart, colend + 1):
            res.append(arr[rowstart][i])

        # Right column
        for i in range(rowstart + 1, rowend + 1):
            res.append(arr[i][colend])

        # Bottom row
        if rowstart < rowend:
            for i in range(colend - 1, colstart - 1, -1):
                res.append(arr[rowend][i])

        # Left column
        if colstart < colend:
            for i in range(rowend - 1, rowstart, -1):
                res.append(arr[i][colstart])

        rowstart += 1 
        rowend -= 1
        colstart += 1
        colend -= 1


if __name__ == '__main__':
    arr = [
        [1,2,3,4], 
        [5,6,7,8], 
        [9,10,11,12], 
        [13,14,15,16]
    ]
    res = SpriralMatrix(arr)
    # print(res)

