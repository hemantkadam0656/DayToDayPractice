from collections import Counter

if __name__ == '__main__':
    X = int(input())  
    shoe_sizes = list(map(int, input().split()))  

    dict = {}
    for idx, num in enumerate(shoe_sizes):
        if num in dict.keys():
            dict[num]= dict.get(num, 0) + 1
        else:
            continue

    inventory = Counter(shoe_sizes)  
    earnings = 0

    customers = int(input())  

    for _ in range(customers):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            earnings += price
            inventory[size] -= 1  

    print(earnings)
