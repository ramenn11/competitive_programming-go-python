n = int(input())

for i in range(1 << n):
    gray = i ^ (i >> 1)
    print(format(gray, f'0{n}b'))

# g_i = b_i XOR b_{i+1}, consecutive bits are XORed, ith bit with (i+1)th and so on