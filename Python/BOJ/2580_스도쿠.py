import sys
sys.stdin = open("input.txt","r")

def get_sqaure(r,c):
    r = r//3 * 3
    c = c//3 * 3
    square = set()
    for _r in range(3):
        for _c in range(3):
            square.add(maps[r + _r][c + _c])
    return square

def sol(zeroes,cur_idx):
    global  flag
    if flag: return
    if cur_idx == len(zeroes):
        flag = True
        [print(*m) for m in maps]

    else:
        cur_r,cur_c,nums = zeroes[cur_idx]
        col = maps_col_by_row[cur_c]
        row = maps[cur_r]
        square = list(get_sqaure(cur_r,cur_c))
        for num in nums:
            if num in col:
                continue
            if num in row:
                continue
            if num in square:
                continue
            maps[cur_r][cur_c] = num
            maps_col_by_row[cur_c][cur_r] = num
            sol(zeroes,cur_idx+1)
            maps[cur_r][cur_c] = 0
            maps_col_by_row[cur_c][cur_r] = 0


base = set(list(range(1, 10)))
maps = [list(map(int,input().split())) for _ in range(9)]
maps_col_by_row = list(map(list,zip(*maps)))
zeroes = []
for r in range(9):
    row = maps[r]
    for c in range(9):
        col = maps_col_by_row[c]
        if maps[r][c] == 0:
            from_row = base - set(row)
            from_col = base - set(col)
            from_square = base - get_sqaure(r,c)
            elements = list(from_row & from_col & from_square)
            zeroes.append([r,c,elements])

flag = False
sol(zeroes,0)

