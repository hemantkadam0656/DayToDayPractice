arr = [8, 7, 3, 3, 4, 4, 3, 3, 1]

target = 3

f = -1
e = -1 

i = 0 
n = len(arr)

while i < n:
    if arr[i] == target and f == -1:
        f = i
    
    if arr[i] == target:
        e = i

    i += 1

print((f,e))
