n = int(input())
res = 0
mul = 5

while mul <= n:
    res += n // mul
    mul *= 5

print(res)