# Backtracking using recursion method

# arr = [1, 2, 3]
# recursion tree (include / exclude each element)

# i = 0, curr = []
# ├── include 1 → curr = [1]
# │   i = 1
# │   ├── include 2 → curr = [1, 2]
# │   │   i = 2
# │   │   ├── include 3 → curr = [1, 2, 3]
# │   │   │   i = 3 → output [1, 2, 3]
# │   │   └── exclude 3 → curr = [1, 2]
# │   │       i = 3 → output [1, 2]
# │   └── exclude 2 → curr = [1]
# │       i = 2
# │       ├── include 3 → curr = [1, 3]
# │       │   i = 3 → output [1, 3]
# │       └── exclude 3 → curr = [1]
# │           i = 3 → output [1]
# └── exclude 1 → curr = []
#     i = 1
#     ├── include 2 → curr = [2]
#     │   i = 2
#     │   ├── include 3 → curr = [2, 3]
#     │   │   i = 3 → output [2, 3]
#     │   └── exclude 3 → curr = [2]
#     │       i = 3 → output [2]
#     └── exclude 2 → curr = []
#         i = 2
#         ├── include 3 → curr = [3]
#         │   i = 3 → output [3]
#         └── exclude 3 → curr = []
#             i = 3 → output []


def AllSubsets(arr,ans,i):
    if i == len(arr):
        for val in ans:
            print(val, end=" ")
        print('\n')
        return 

    ans.append(arr[i])
    AllSubsets(arr, ans, i+1)
    ans.pop()
    AllSubsets(arr, ans, i+1)


if __name__ == '__main__':
    arr = [1,2,3]
    ans = []
    i = 0
    res = AllSubsets(arr,ans,i)


