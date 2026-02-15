board = [input().strip() for _ in range(8)]

res = 0
col = [False] * 8
d1 = [False] * 15
d2 = [False] * 15

def backtrack(r):
    global res
    if r == 8:
        res += 1
        return
    
    for c in range(8):
        if board[r][c] == '.' and not col[c] and not d1[r+c] and not d2[r-c+7]:
            col[c] = d1[r+c] = d2[r-c+7] = True
            backtrack(r + 1)
            col[c] = d1[r+c] = d2[r-c+7] = False


backtrack(0)
print(res)