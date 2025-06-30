
def SumOfAllNaturalNum(n):
    sum = 0
    x = 1 

    while x <= n:
        sum += x
        x += 1
    return sum
        
if __name__ == '__main__':
    n = int(input('Enter natual number to get sum : '))
    print(SumOfAllNaturalNum(n))

    


