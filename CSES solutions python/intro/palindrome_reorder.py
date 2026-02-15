from collections import Counter

s = input().strip()
freq = Counter(s)

odd_chars = [c for c in freq if freq[c] % 2 == 1]

if len(odd_chars) > 1:
    print("NO SOLUTION")
else:
    first_half = []
    middle = ""

    for c in sorted(freq):
        first_half.append(c * (freq[c] // 2))
        if freq[c] % 2 == 1:
            middle = c

    first_half = "".join(first_half)
    print(first_half + middle + first_half[::-1])