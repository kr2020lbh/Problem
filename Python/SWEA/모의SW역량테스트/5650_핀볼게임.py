import sys
sys.stdin = open("input.txt","r")

def init():
    for i in range(N):
        for j in range(N):
            if maps[i][j] in [6,7,8,9,10]:
                worm_holes[maps[i][j]].append([i,j])
            if maps[i][j] == 0:
                start_points.append([i,j])


def pin_ball(sr,sc,d):
    global ans
    nr,nc = sr+dr[d],sc+dc[d]
    tmp = 0
    while True:
        #maps의 테두리를 만났을 때
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            tmp += 1
            d = (d+2) % 4
            nr += dr[d]
            nc += dc[d]
            continue

        #시작점으로 돌아오거나, 블랙홀을 만났을 때
        if nr == sr and nc == sc or maps[nr][nc] == -1:
            ans = max(ans,tmp)
            break

        if maps[nr][nc] == 0:
            nr += dr[d]
            nc += dc[d]
            continue

        #웜홈을 만났을 때
        if maps[nr][nc] in [6,7,8,9,10]:
            points = worm_holes[maps[nr][nc]]
            if points[0] == [nr,nc]:
                nr,nc = points[1]
            else:
                nr,nc = points[0]
            nr += dr[d]
            nc += dc[d]
            continue

        #1,2,3,4,5를 만났을 때
        if maps[nr][nc] in [1,2,3,4,5]:
            if maps[nr][nc] == 1:
                if d == 0:
                    d = 1
                elif d == 3:
                    d = 2
                else:
                    d = (d+2) % 4
            elif maps[nr][nc] == 2:
                if d == 2:
                    d = 1
                elif d == 3:
                    d = 0
                else:
                    d = (d+2) % 4
            elif maps[nr][nc] == 3:
                if d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = (d+2) % 4
            elif maps[nr][nc] == 4:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                else:
                    d = (d+2) % 4
            elif maps[nr][nc] == 5:
                d = (d+2) % 4

            tmp += 1
            nr += dr[d]
            nc += dc[d]


dr = [1,0,-1,0] #하 우 상 좌
dc = [0,1,0,-1]
T = int(input())

for tc in range(1,T+1):
    ans = 0
    N = int(input())
    maps = [list(map(int,input().split())) for _ in range(N)]
    worm_holes =[[] for _ in range(11)]
    start_points = []
    init()
    for sr,sc in start_points:
        for d in range(4):
            pin_ball(sr,sc,d)
    print("#{} {}".format(tc,ans))