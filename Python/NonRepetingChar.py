string = 'KadamhKadam'

dict = {}

for i in string:
    dict[i] = string.count(i)

for key, value in dict.items():
    if dict[key] == 1:
        print(key)
        break
