import sys,copy
sys.stdin = open("input.txt","r")
def move(d,maps,balls):
    global ans
    sorted_balls = get_order(d,balls)
    if d == 0: #위로 기울기 그러면, 위쪽을 먼저 탐색해야한다.
        for row,col in sorted_balls:
            for k in range(col-1,-1,-1):
                if maps[row][k]!="#":
                    if maps[row][k] == 'O':
                        pass
                    elif maps[row][k] == 'R' or maps[row][k] == 'B':
                        break
    if d == 1:  # 오른쪽으로 기울기, 그러면 오른쪽을 먼저 탐색해야한다.
    if d == 2:#아래로 기울기 그러면 아래쪽을 먼저 탐색해야한다.
    if d == 3:  # 왼쪽으로 기울기, 그러면 왼쪽을 먼저 탐색해야한다


def get_order(d,balls):
    if red[0] == blue[0]:
        if d == 1: #오른쪽이면 열 내림차순
            return sorted(balls, key=lambda x:-x[1])
        if d == 3: #왼쪽이면 열 오름차순
            return sorted(balls, key=lambda x:x[1])
    if red[1] == blue[1]:
        if d== 0: #위쪽이면, 행 오름차순
            return sorted(balls, key=lambda x:x[0])
        if d== 2: #아래쪽이면, 행 오름차순
            return sorted(balls, key=lambda x:-x[0])
    return balls

def tilt(maps,depth,balls):
    if depth == 10:
        return
    else:
        for d in range(4):
            next_maps = copy.deepcopy(maps)
            move(d,next_maps,balls)
            tilt(next_maps,depth+1)


N,M = map(int,input().split())
maps = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'O':
            hole = [i,j]
        if maps[i][j] == 'R':
            red = [i,j]
        if maps[i][j] == 'B':
            blue = [i,j]
ans = 11
tilt(maps,0,[red,blue])
print(ans)
