s = input().strip()

max_len = 1
curr = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        curr += 1
    else:
        max_len = max(max_len, curr)
        curr = 1

max_len = max(max_len, curr)

print(max_len)