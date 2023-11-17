n = int(input())
nums = list(map(int, input().split()))


def check(arr):
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            return "NO"
        i += 1
    return "YES"


print(check(nums))
