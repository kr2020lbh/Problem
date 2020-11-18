import sys
sys.stdin = open("input.txt","r")

def clean(r,c,d):
    if visited[r][c] == 0:
        visited[r][c] = 1
    cnt = 1
    while True:
        for i in range(1,5):
            tmp_d = (d-i) % 4
            dr = r + d_row[tmp_d]
            dc = c + d_col[tmp_d]
            if visited[dr][dc]==0 and area[dr][dc] == 0:
                visited[dr][dc] = 1
                r,c = dr,dc
                d = tmp_d
                cnt += 1
                break
        else:
            tmp_d = (d-2) % 4
            r += d_row[tmp_d]
            c += d_col[tmp_d]
            if area[r][c] == 1:
                return cnt


d_row = [-1,0,1,0]
d_col = [0,1,0,-1]
N,M = map(int,input().split())
r,c,d = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

print(clean(r,c,d))
