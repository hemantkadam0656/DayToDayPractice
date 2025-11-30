# The below approch is usefull to get the majority element by using optimized way

def MajorityElements(arr):
    sorted_arr = sorted(arr)
    n = len(arr)

    freq = 1
    ans = 0
    for i in range(n):
        if sorted_arr[i] == sorted_arr[i-1]:
            freq += 1
        else:
            freq = 1
            ans = sorted_arr[i]
        
        if freq > (n//2):
            return ans


if __name__ == "__main__":
    arr = [1,2,2,2,3,3,3,3,3,3,3,3,3]
    res = MajorityElements(arr)
    print(res)


def MooresVotingAlgo(arrSec):
    n = len(arrSec)
    freqency = 0
    answer = 0
    for i in range(n):
        if freqency == 0:
            answer = arrSec[i]
        elif answer == arrSec[i]:
            freqency += 1
        else:
            freqency -= 1

    if freqency > (n // 2):
        return answer
    else:
        return -1 



if __name__ == "__main__":
    arrSec =  [1,2,2,2,4,4,4,4,4,4,4,4]
    result = MooresVotingAlgo(arrSec)
    print(result)






