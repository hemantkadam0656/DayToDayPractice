string = 'BANANA'
vowels = 'AEIOU'
kevin_score = 0
stuart_score = 0

for i in range(len(string)):
    if string[i] in vowels:
        print(string[i])
        kevin_score += len(string) - i
    else:
        stuart_score += len(string) - i

if kevin_score > stuart_score:
    print("Kevin", kevin_score)
elif stuart_score > kevin_score:
    print("Stuart", stuart_score)
else:
    print("Draw")