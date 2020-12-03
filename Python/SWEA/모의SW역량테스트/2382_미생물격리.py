import sys
sys.stdin = open("input.txt","r")

d_r = [-1,0,1,0]
d_c = [0,1,0,-1]

for t in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    maps = [ [[] for _ in range(N)] for _ in range(N)]
    indexes = []

    for _ in range(K):
        r,c,num,direction = map(int,input().split())
        if direction == 1:
            direction = 0
        elif direction == 4:
            direction = 1
        maps[r][c].append([num,direction])
        indexes.append([r,c])

    while M!=0:
        new_index = set()
        for r,c in indexes:
            num,direction = maps[r][c][0]
            dr, dc = r + d_r[direction], c + d_c[direction]
            if dr == 0 or dr == N-1 or dc == 0 or dc == N-1:
                num = num //2
                if num != 0:
                    maps[dr][dc].append([num,(direction+2)%4])
                    new_index.add((dr,dc))
            else:
                maps[dr][dc].append([num, direction])
                new_index.add((dr,dc))
            maps[r][c].pop(0)

        for r,c in new_index:
            if len(maps[r][c]) > 1:
                sumation = 0
                max_num = 0
                for i in range(len(maps[r][c])):
                    num,direction = maps[r][c][i]
                    sumation += num
                    if max_num < num:
                        max_num = num
                        max_direction = direction
                maps[r][c] = [[sumation,max_direction]]

        M-=1
        indexes = new_index

    ans = 0
    for r,c in indexes:
        ans += maps[r][c][0][0]
    print("#{} {}".format(t,ans))
