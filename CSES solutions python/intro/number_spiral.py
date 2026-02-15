import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    serial = max(n, m)

    if serial % 2 == 0:
        n, m = m, n

    if n <= m:
        print((serial - 1) * (serial - 1) + n)
    else:
        print((serial - 1) * (serial - 1) + 2 * serial - m)