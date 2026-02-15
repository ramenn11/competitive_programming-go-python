s = input().strip()
s = sorted(s)
n = len(s)
result = []
used = [False] * n

def backtrack(path, used):
    if len(path) == len(used):
        result.append("".join(path))

    for i in range(n):
        if used[i]:
            continue
        
    # Prevents generating duplicate branches
        if i > 0 and s[i] == s[i-1] and not used[i-1]:
            continue

        path.append(s[i])
        used[i] = True
        backtrack(path, used)
        path.pop()
        used[i] = False

backtrack([], used)
print(len(result))
for r in result:
    print(r)