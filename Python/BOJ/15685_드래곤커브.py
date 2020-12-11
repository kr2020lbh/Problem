import sys
sys.stdin = open("input.txt","r")
#회전은 기준점을 0,0 으로 만들고 -1 곱하고 다시 원래 기준점으로 돌아간다.
#만약 기준점이 m,n 이고 회전시켜야할 점이 a,b라면
#기준점을 0,0으로, 회전시킬 점을 a-m,b-n으로 만든 후 회전
# m-a, n-b 그리고 다시 원래 점으로 이동, 2m-a, 2n-b 가 된다.
N = int(input())
maps = [[0]*101 for _ in range(101)]
delta = [[0,1],[-1,0],[0,-1],[1,0]]
for _ in range(N):
    col,row,d,g = map(int,input().split()) #x는 col y는 row
    drow, dcol = row+delta[d][0], col+delta[d][1]
    maps[row][col] = 1
    maps[drow][dcol] = 1
    indexes = [[row,col]]
    end = [drow, dcol]
    for _ in range(g):
        pivot_row,pivot_col = end
        tmp_index = []
        while indexes:
            row,col = indexes.pop(0)
            maps[pivot_row-pivot_col+col][pivot_row+pivot_col-row] = 1
            tmp_index.append([pivot_row-pivot_col+col,pivot_row+pivot_col-row])
            tmp_index.append([row,col])
        tmp_index.append(end)
        end = tmp_index.pop(0)
        indexes = tmp_index

ans = 0
for i in range(100):
    for j in range(100):
        if maps[i][j] == 1:
            if maps[i+1][j] == 1 and maps[i][j+1] == 1 and maps[i+1][j+1] == 1:
                ans += 1
print(ans)