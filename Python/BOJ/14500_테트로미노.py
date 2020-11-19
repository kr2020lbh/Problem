import sys
sys.stdin = open("input.txt","r")

def move(x,y,res):
    for i in range(len(blocks)):
        tmp = 0
        for j in range(4):
            try:
                d_x = x + blocks[i][j][0]
                d_y = y + blocks[i][j][1]
                tmp += arr[d_x][d_y]
                if res < tmp:
                    res = tmp
            except:
                continue
    return res
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
blocks = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

for x in range(N):
    for y in range(M):
        result = move(x,y,result)
print(result)
