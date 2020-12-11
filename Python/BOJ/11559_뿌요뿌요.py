import sys
sys.stdin = open("input.txt","r")

def check():
    visited = [[0]*6 for _ in range(12)]
    global  cnt

    indexes = []
    for r in range(11,-1,-1):
        for c in range(6):
            me = maps[r][c]
            tmp_indexes = [[r, c]]
            if me != '.':
                visited[r][c] = 1
                Q = [[r, c]]
                while Q:
                    tmp_r, tmp_c = Q.pop(0)
                    for k in range(4):
                        dr = tmp_r + d_r[k]
                        dc = tmp_c + d_c[k]
                        if 0 <= dr < 12 and 0 <= dc < 6 and not visited[dr][dc]:
                            you = maps[dr][dc]
                            if me == you:
                                Q.append([dr, dc])
                                visited[dr][dc] = 1
                                tmp_indexes.append([dr, dc])

            if len(tmp_indexes) >= 4:
                indexes.extend(tmp_indexes)
    for r, c in indexes:
        maps[r][c] = '.'
    for col in range(6):
        new_col = []
        for row in range(11, -1, -1):
            if maps[row][col] != '.':
                new_col.append(maps[row][col])
        new_col += (12 - len(new_col)) * '.'
        for r in range(12):
            maps[r][col] = new_col[-1 - r]
    if indexes:
        cnt += 1
        check()



d_r = [1,-1,0,0]
d_c = [0,0,1,-1]
cnt = 0
maps = [list((input())) for _ in range(12)]
check()
print(cnt)