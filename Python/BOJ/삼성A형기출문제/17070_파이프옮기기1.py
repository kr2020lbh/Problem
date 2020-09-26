import sys
sys.stdin = open("input.txt","r")

def build_pipe(prev_pipe,r,c):
    global cnt
    if r==n-1 and c==n-1:
        cnt += 1
    else:
        if prev_pipe == 1 or prev_pipe == 3:
            if c+1 < n and house[r][c+1] == 0:
                build_pipe(1,r,c+1)
        if prev_pipe == 2 or prev_pipe == 3:
            if r+1 < n and house[r+1][c] == 0:
                build_pipe(2,r+1,c)
        if r+1 < n and c+1 < n :
            if house[r+1][c] == house[r][c+1] == house[r+1][c+1] == 0:
                build_pipe(3,r+1,c+1)


n = int(input())
house = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
build_pipe(1,0,1)
print(cnt)