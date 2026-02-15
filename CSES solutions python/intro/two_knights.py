n = int(input())

def nc2(x):
    return x * (x-1) // 2

for k in range(1, n+1):
    total = nc2(k * k)
    attacking = 4 * (k-1)*(k-2)
    print(total - attacking)