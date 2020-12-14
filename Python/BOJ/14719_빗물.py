import sys
sys.stdin = open("input.txt","r")
H,W = map(int,input().split())
walls = list(map(int,input().split()))
maps = [[0]*W for _ in range(H)]
for i in range(W):
    wall = walls[i]
    for h in range(H-1,H-wall-1,-1):
        maps[h][i] = 1

ans = 0
for row in range(H-1,-1,-1):
    flags =[]
    for col in range(W):
        if maps[row][col] == 1:
            flags.append(col)
    if len(flags) > 1:
        for i in range(len(flags)-1):
            ans += flags[i+1] - flags[i] - 1
print(ans)

