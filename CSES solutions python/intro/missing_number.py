n = int(input())
nums = list(map(int, input().split()))

exp = n * (n + 1) // 2
total = sum(nums)

print(exp - total)