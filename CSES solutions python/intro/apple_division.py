import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = sum(arr)
limit = 1 << n

for mask in range(limit):
    temp = 0
    for i in range(n):
        if mask & (1 << i):
            temp += arr[i]
        else:
            temp -= arr[i]
            
    res = min(res, abs(temp))

print(res)