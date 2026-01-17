def IntersectionArray(nums1, nums2):
    freqency = {}
    result = []

    for num in nums1:
        freqency[num] = freqency.get(num, 0)+ 1

    print(freqency)

    for num in nums2:
        if num in freqency and freqency[num] > 0 :
            result.append(num)
            freqency[num] -= 1

        print(freqency)

    return result


if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = IntersectionArray(nums1, nums2)
    print(res)