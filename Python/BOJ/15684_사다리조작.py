import sys
from itertools import combinations
sys.stdin = open("input.txt","r")


def sol(ladder_cnt):
    for loc in combinations(indexes,ladder_cnt):
        put_ladder(loc,1)
        if go_ladder():return True
        put_ladder(loc,0)
    return False

def put_ladder(loc,loc_val):
    for x, y in loc:
        ladders[x][y] = loc_val
        ladders[x][y + 1] = -loc_val

def go_ladder():
    index = 0
    while index < N:
        col = index
        row = 0
        while row <= H:
            if row == H:
                if index != col:
                    return False
                break
            if ladders[row][col] == 1:
                    col += 1
            elif ladders[row][col] == -1:
                    col -= 1
            row += 1
        index += 1
    return True


N,M,H = map(int,input().split())
ladders = [[0]*N for _ in range(H)]
indexes = []

for _ in range(M):
    x,y = map(int,input().split())
    ladders[x-1][y-1] = 1
    ladders[x-1][y] = -1

for x in range(H):
    for y in range(N):
        if y+1 < N and ladders[x][y]==0 and ladders[x][y+1] == 0 :
            indexes.append([x,y])


#0행 c 열에서 시작한다
#각각 c열에서 밑으로 떨어지면서 1이 있으면 다음 열로 이동한다
#그러다가 마지막 행이 되었을 떄, 자기 자신의 열을 반환하여 모두 자기 열이 되면 옳은 것!
#3개까지 놓고 그 이후는 -1로..
for ladder_cnt in range(4):
    if sol(ladder_cnt):
        print(ladder_cnt)
        break
else:
    print(-1)
