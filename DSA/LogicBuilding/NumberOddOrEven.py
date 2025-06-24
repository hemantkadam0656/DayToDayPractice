def Odd_Even_num(n):

    if n % 2 == 0 :
        return f'A given number {n} is Even number.'
    elif n % 2 != 0:
        return f'A given number {n} is Odd number.'


if __name__ == '__main__':
    number = int(input('Enter your number : '))
    res = Odd_Even_num(number)
    print(res)


