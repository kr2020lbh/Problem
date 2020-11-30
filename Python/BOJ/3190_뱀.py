import sys
sys.stdin = open("input.txt","r")

d_x = [0,1,0,-1]
d_y = [1,0,-1,0]

N = int(input()) #행렬 크기
maps = [[0]*N for _ in range(N)]

K = int(input()) #사과 개수
for _ in range(K):
    x,y = map(int,input().split())
    maps[x-1][y-1] = 1

L = int(input()) #방향 변환 횟수 (정수, 알파벳) 시간초가 지난 후 L(왼),D(오)로 90도 회전한다는 뜻
directions = [0] * 10001
for _ in range(L):
    time,direction = input().split()
    if direction == 'L':
        direction = -1
    else:
        direction = 1
    directions[int(time)] = direction

cnt = cur_dir = 0
cur_x=cur_y=0
maps[cur_x][cur_y] = -1
LAST = [[0,0]]
while True:
    if directions[cnt]:
        cur_dir = (cur_dir + directions[cnt])%4
    next_x = cur_x + d_x[cur_dir]
    next_y = cur_y + d_y[cur_dir]
    # [print(m) for m in maps]
    # print(cnt,directions[cnt])
    # print(cur_dir)
    # print(next_x,next_y)
    if next_x < 0 or N<= next_x or next_y < 0 or N <= next_y:
        break
    if maps[next_x][next_y] == -1:
        break
    if maps[next_x][next_y] == 1:
        maps[next_x][next_y] = -1
    else:
        maps[next_x][next_y] = -1
        last_x,last_y = LAST.pop(0)
        maps[last_x][last_y] = 0
    cur_x, cur_y = next_x,next_y
    LAST.append([cur_x, cur_y])
    cnt += 1

print(cnt+1)