def FourSum(arr):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n):
        if (i>0 and arr[i] == arr[i-1]):continue

        for j in range(i+1, n-2):
            if (j>0 and arr[j] == arr[j-1]): continue
                
            p = j+1
            q = n-1

            while(p<q):

                sum = arr[i]+arr[j]+arr[p]+arr[q]
                        # -2 -1 + 1 + 2
                if sum == target:
                    result.append((arr[i], arr[j], arr[p], arr[q]))
                    p += 1
                    q -= 1       

                    while (p > j+2 and arr[p] == arr[p-1]): p+=1   
                    while p < q and arr[q] == arr[q + 1]: q -= 1  
                            
                elif sum > target:
                    q -= 1
                else:
                    p += 1

    return result
if __name__ == '__main__':
    arr = [-2, -1, -1, 1, 1, 2, 2]
    target = 0
    res = FourSum(arr)
    print(res)



