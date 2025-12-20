# To find the greatest common divisor (GCD) of numbers, we can divide number by numbers starting from 1,2,3,4,5,6,.......number 
# There is another method called Euclid's Algorithm, which help's to find the common divider of two numbers by dividing the number with smaller number.
# To find the Least common divisor (LCD) of numbers, we can divide the multiplication of number with GCD  
def GCD(a,b):
    while(a > 0 and b > 0):
        if a > b:
            a = a % b 
        else:
            b = b % a
    
    return b if a == 0 else a 

def LCD(a,b):
    gcd = GCD(a,b)
    return (a * b)// gcd


if __name__ == '__main__':
    a = 20
    b = 28
    res = LCD(a,b)
    print(res)
