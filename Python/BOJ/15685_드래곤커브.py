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
    x,y,d,g = map(int,input().split()) #x는 col y는 row
    maps[y][x] = 1
    dx = x+delta[d][1]
    dy = y+delta[d][0]
    end = [dy,dx]
    maps[dy][dx] = 1
    indexes = [[y,x]]
    for _ in range(g):
        pivot_y,pivot_x = end
        print('기준점',end)
        print(indexes)
        tmp_index = []
        for x,y in indexes:
            maps[pivot_x+pivot_y-y][pivot_x+pivot_y-x] = 1
            tmp_index.append([pivot_x+pivot_y-x,pivot_x+pivot_y-y])
        tmp_index.append(end)
        end = tmp_index[0]
        indexes = tmp_index
[print(m) for m in maps]


