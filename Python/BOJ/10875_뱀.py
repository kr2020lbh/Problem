import sys
sys.stdin = open("input.txt","r")
L = int(input())
maps = [[0]*(2*L+1) for _ in range(2*L+1)]
maps[L][L] = 1
N = int(input())
cur_d = 0 #오른쪽
cur_r,cur_c = L,L
delta = [[0,1],[1,0],[0,-1],[-1,0]]
cnt = 0
hor = dict()
ver = dict()
for _ in range(N):
    print(cur_r,cur_c)
    t,d = input().split()
    t = int(t)
    next_r,next_c = cur_r + t * delta[cur_d][0], cur_c + t * delta[cur_d][1]
    if cur_d == 0 or cur_d == 2: #오른쪽 혹은 왼쪽, 수평 선분
        pass
    else: #위쪽 혹은 아럐쪽, 수직 선분
        pass
    cur_r, cur_c = next_r, next_c


    if d == 'R':
        cur_d = (cur_d+1) % 4
    else:
        cur_d = (cur_d-1) % 4
print(cur_r,cur_c)

[print(m) for m in maps]