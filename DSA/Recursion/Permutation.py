def Permutations(nums, idx, ans):
    if idx == len(nums):
        ans.append(nums.copy())
        return ans

    for i in range(idx, len(nums)):
        nums[idx], nums[i] = nums[i], nums[idx]
        Permutations(nums, idx+1, ans)
        nums[idx], nums[i] = nums[i], nums[idx]

if __name__ == '__main__':
    nums = [1,2,3]
    idx = 0
    ans = []
    
    res = Permutations(nums, idx, ans)
    print(ans)



# Level idx = 0
# [1, 2, 3]
# │
# ├── swap(0,0) → [1, 2, 3]
# │   └── idx = 1
# │       │
# │       ├── swap(1,1) → [1, 2, 3]
# │       │   └── idx = 2
# │       │       └── swap(2,2) → [1, 2, 3]
# │       │           ✔ store [1, 2, 3]
# │       │
# │       └── swap(1,2) → [1, 3, 2]
# │           └── idx = 2
# │               └── swap(2,2) → [1, 3, 2]
# │                   ✔ store [1, 3, 2]
# │
# ├── swap(0,1) → [2, 1, 3]
# │   └── idx = 1
# │       │
# │       ├── swap(1,1) → [2, 1, 3]
# │       │   └── idx = 2
# │       │       └── swap(2,2) → [2, 1, 3]
# │       │           ✔ store [2, 1, 3]
# │       │
# │       └── swap(1,2) → [2, 3, 1]
# │           └── idx = 2
# │               └── swap(2,2) → [2, 3, 1]
# │                   ✔ store [2, 3, 1]
# │
# └── swap(0,2) → [3, 2, 1]
#     └── idx = 1
#         │
#         ├── swap(1,1) → [3, 2, 1]
#         │   └── idx = 2
#         │       └── swap(2,2) → [3, 2, 1]
#         │           ✔ store [3, 2, 1]
#         │
#         └── swap(1,2) → [3, 1, 2]
#             └── idx = 2
#                 └── swap(2,2) → [3, 1, 2]
#                     ✔ store [3, 1, 2]


