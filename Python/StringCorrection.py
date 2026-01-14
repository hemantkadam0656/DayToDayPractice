def StringCorrection(string):
    words = string.split()

    words.sort(key = lambda w: int(''.join(filter(str.isdigit, w))))

    words = [''.join(filter(str.isalpha ,w)) for w in words]

    newString = " ".join(words)

    print(newString)


if __name__ == '__main__':
    IP_string = "is1 Thi0s T3est 2a"
    res = StringCorrection(IP_string)