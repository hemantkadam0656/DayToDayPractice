
def MissingAndReapetingValue(grid):
    n = len(grid)
    m = len(grid[0])
    list = []
    a = 0
    b = 0
    actual_sum = 0
    
    for i in range(n):
        for j in range(m):
            actual_sum += grid[i][j]
            if grid[i][j] in list:
                a =  grid[i][j]
            else:
                list.append(grid[i][j])
    
    except_sum = ((n*n)*(n*n+1) )// 2

    b = except_sum + a - actual_sum

    return (a,b)
  

if __name__ == '__main__':
    arr = [
        [9,1,7],
        [8,9,2],
        [3,4,6]
    ]

    res = MissingAndReapetingValue(arr)
    print(res)


