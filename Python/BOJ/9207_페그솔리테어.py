import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10**6)
def dfs(depth):
    flag = False
    for row in range(5):
        for col in range(9):
            if maps[row][col] == 'o':
                for k in range(4):
                    dr = row + d_row[k]
                    dc = col + d_col[k]
                    if 0<= dr < 5 and 0<= dc < 9 and maps[dr][dc] == 'o':
                        _dr = dr + d_row[k]
                        _dc = dc + d_col[k]
                        if 0<= _dr < 5 and 0<= _dc < 9 and maps[_dr][_dc] == '.':
                            flag = True
                            maps[row][col] = '.'
                            maps[dr][dc] = '.'
                            maps[_dr][_dc] = 'o'
                            dfs(depth+1)
                            maps[row][col] = 'o'
                            maps[dr][dc] = 'o'
                            maps[_dr][_dc] = '.'
    if flag == False:
        cnt = 0
        for i in range(5):
            for j in range(9):
                if maps[i][j] == 'o':
                    cnt += 1
        if depth < left_pin[cnt-1]:
            left_pin[cnt-1] = depth


N = int(input())
d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
for _ in range(N):
    left_pin = [10 ** 6] * 8
    maps = [list(input()) for _ in range(5)]
    if _ != N-1:enter = input()
    dfs(0)
    for i in range(8):
        if left_pin[i] != 10 ** 6:
            print(i+1,left_pin[i])
            break
