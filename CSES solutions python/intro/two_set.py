n = int(input())
total = n * (n + 1) // 2

if total % 2 != 0:
    print("NO")
else:
    print("YES")
    target = total // 2
    seen = [False] * (n + 1)
    set1 = []
    
    for i in range(n, 0, -1):
        if target >= i:
            set1.append(i)
            seen[i] = True
            target -= i

    set2 = []
    for i in range(1, n + 1):
        if not seen[i]:
            set2.append(i)

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
