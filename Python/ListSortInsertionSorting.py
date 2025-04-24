def main(list): 
    n = len(list)

    if n <= 1:
        return 
    

    
    for i in range(1, n):
        print(list[1])
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1

        list[j + 1] = key 

    return list
    
if __name__ == '__main__':
    list = [4,6,7,8,1,2,5,2,32,76,12,76,9]
    print(main(list))
