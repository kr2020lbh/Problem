import sys
sys.stdin = open("input.txt","r")

def gravity(block,x,y):
    if block == 1:
        #세로로 떨어지기
        nx = x
        while True:
            if nx == 10:
                maps[nx-1][y] = 1
                break    
            if maps[nx][y]:
                maps[nx-1][y] = 1
                break
            nx += 1
        
        #가로로 떨어지기
        ny = y
        while True:
            if ny == 10:
                maps[x][ny-1] = 1
                break    
            if maps[x][ny]:
                maps[x][ny-1] = 1
                break
            ny += 1
            
    if block == 2:
        #세로로 떨어지기
        nx = x
        while True:
            if nx == 10:
                maps[nx-1][y] = 1
                maps[nx-1][y+1] = 1
                break    
            if maps[nx][y] or maps[nx][y+1]:
                maps[nx-1][y] = 1
                maps[nx-1][y+1] = 1
                break
            nx += 1
        
        #가로로 떨어지기
        ny = y
        while True:
            if ny == 10:
                maps[x][ny-1] = 1
                maps[x][ny-2] = 1
                break    
            if maps[x][ny]:
                maps[x][ny-1] = 1
                maps[x][ny-2] = 1
                break
            ny += 1
            
    if block == 3:
        #세로로 떨어지기
        nx = x
        while True:
            if nx == 10:
                maps[nx-1][y] = 1
                maps[nx-2][y] = 1
                break    
            if maps[nx][y]:
                maps[nx-1][y] = 1
                maps[nx-2][y] = 1
                break
            nx += 1
        
        #가로로 떨어지기
        ny = y
        while True:
            if ny == 10:
                maps[x][ny-1] = 1
                maps[x+1][ny-1] = 1
                break    
            if maps[x][ny] or maps[x+1][ny]:
                maps[x][ny-1] = 1
                maps[x+1][ny-1] = 1
                break
            ny += 1

def check_row():
    global cnt
    _r = []
    for r in range(4,10):
        if sum(maps[r][0:4]) == 4:
            cnt += 1
            for _r in range(r,3,-1):
                for c in range(0,4):
                    maps[_r][c] = maps[_r-1][c]
            

def check_col():
    global cnt
    for c in range(4,10):
        sumation = 0
        for i in range(0,4):
            if not maps[i][c]:
                break
        else:
            cnt += 1
            for _c in range(c,3,-1):
                for i in range(0,4):
                    maps[i][_c] = maps[i][_c-1]


def check_row_clean_zone():
    row_cnt = 0
    for i in range(4,6):
        for j in range(0,4):
            if maps[i][j]:
                row_cnt += 1
                break
    for r in range(9,3,-1):
        for c in range(0,4):
            maps[r][c] = maps[r-row_cnt][c]

def check_col_clean_zone():
    col_cnt = 0
    for j in range(4,6):
        for i in range(0,4):
            if maps[i][j]:
                col_cnt += 1
                break
    for c in range(9,3,-1):
        for r in range(0,4):
            maps[r][c] = maps[r][c-col_cnt]


maps = [[0]*10 for _ in range(10)]
N = int(input())
cnt = 0
for _ in range(N):
    t,x,y = map(int,input().split())
    gravity(t,x,y)
    check_row()
    check_col()
    check_row_clean_zone()
    check_col_clean_zone()
ans = 0
for i in range(10):
    for j in range(10):
        if maps[i][j]:
            ans += 1
print(cnt)
print(ans)

