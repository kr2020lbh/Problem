import sys
sys.stdin = open("input.txt","r")


def move(d):
    global r,c
    d_r,d_c = d_move[d]
    dr = r+d_r
    dc = c+d_c
    if 0<= dr < N and 0<= dc < M:
        if d == 0: #동쪽굴리기
            dice[1] = [dice[1][2]] + dice[1][0:2]
            dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
        if d == 1: #서쪽굴리기
            dice[1] = dice[1][1:3] + [dice[1][0]]
            dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
        if d == 2: #북쪽굴리기
            for k in range(3,0,-1):
                dice[k][1],dice[k-1][1] = dice[k-1][1],dice[k][1]
        if d == 3: #남쪽굴리기
            for k in range(3):
                dice[k][1],dice[k+1][1] = dice[k+1][1], dice[k][1]

        if maps[dr][dc] == 0:
            maps[dr][dc] = dice[3][1]
        else:
            dice[3][1] = maps[dr][dc]
            maps[dr][dc] = 0
        print(dice[1][1])
        r,c = dr,dc


N,M,r,c,K = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
commands = list(map(int,input().split()))
d_move = [[0,1],[0,-1],[-1,0],[1,0]]
dice = [[0]*3 for _ in range(4)]
for command in commands:
    move(command-1)
