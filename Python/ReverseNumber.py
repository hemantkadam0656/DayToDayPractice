num = +12345678
total = 0

if num != 0 :
    for i in range(len(str(num))):
        count = num % 10
        num = num // 10
        total += count 

print(total)