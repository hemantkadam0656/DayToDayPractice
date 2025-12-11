
def MergeSortedArray(A,B,m,n):
    l = m+n
    idx = m+n-1 
    i = m-1 
    j = n-1

    while i >= 0 and j >=0:
        if A[i] >= B[j]:
            A[idx] = A[i]
            i -= 1
            idx -= 1
        else:
            A[idx] = B[j]
            j -= 1
            idx-= 1
    
    while j >= 0:
        A[idx] = B[j]
        j -=1
        idx -= 1

    return A
        

if __name__ == '__main__':
    A = [4,5,6,0,0,0,0]
    B = [1,2,3,7]
    m = 3
    n = 4 
    res = MergeSortedArray(A,B,m,n)
    print(res)



