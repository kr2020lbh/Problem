import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N = int(input())
    rows = [[] for _ in range(2001)]
    cols = [[] for _ in range(2001)]
    maps = [[0]*2001 for _ in range(2001)]
    d_x = [-1,1,0,0]
    d_y = [0,0,-1,1]
    indexes = []
    for _ in range(N):
        x,y,direction,energy = map(int,input().split())
        x+=1000
        y+=1000
        rows[x].append(y)
        cols[y].append(x)
        maps[x][y] = [energy,direction]
        indexes.append([x,y])
    collisions = []

    for x,y in indexes:
        min_dist = 2000
        energy,direction = maps[x][y]
        if direction == 0: #나는 위로방향 아래로 방향을 찾아라
            for dx in cols[y]:
                if dx != x and dx < x:
                    d_energy,d_direction = maps[dx][y]
                    if d_direction == 1:
                        collisions.append([x,y,dx,y,energy,d_energy,abs(x-dx)])
                        if min_dist > abs(x-dx):
                            min_dist = abs(x-dx)
            # min_dist 과 같거나 더 작은 좌상 우상이 존재하는가?
            flag = False
            for k in range(1,min_dist+1): #좌상 그리고 오른쪽으로 움직이는 것 찾아라
                d_x1,d_y1 = x-k,y-k #좌상
                d_x2,d_y2 = x-k,y+k #우상
                if 0<= d_x1 < 2001 and 0<= d_y1 < 2001:
                    if maps[d_x1][d_y1] != 0:
                        d_energy, d_direction = maps[d_x1][d_y1]
                        if d_direction == 3:
                            collisions.append([x, y, d_x1, d_y1, energy, d_energy])
                            flag = True

                if 0<= d_x2 < 2001 and 0<= d_y2 < 2001: #우상 그리고 왼쪾으로 움직이는 것 찾아라
                    if maps[d_x2][d_y2] != 0:
                        d_energy, d_direction = maps[d_x2][d_y2]
                        if d_direction == 3:
                            collisions.append([x, y, d_x2, d_y2, energy, d_energy])
                            flag = True
                if flag:
                    break

        if direction == 1: #나는 아래방향, 위로 방향을 찾아라
            for dx in cols[y]:
                if dx != x and dx > x:
                    d_energy,d_direction = maps[dx][y]
                    if d_direction == 0:
                        collisions.append([x,y,dx,y,energy,d_energy,abs(x-dx)])
                        if min_dist > abs(x-dx):
                            min_dist = abs(x-dx)
            # min_dist 과 같거나 더 작은 좌하 우하 존재하는가?
            flag = False
            for k in range(1, min_dist + 1):  # 좌하 그리고 오른쪽으로 움직이는 것 찾아라
                d_x1, d_y1 = x + k, y - k  # 좌하
                d_x2, d_y2 = x + k, y + k  # 우하
                if 0 <= d_x1 < 2001 and 0 <= d_y1 < 2001:
                    if maps[d_x1][d_y1] != 0:
                        d_energy, d_direction = maps[d_x1][d_y1]
                        if d_direction == 3:
                            collisions.append([x, y, d_x1, d_y1, energy, d_energy])
                            flag = True

                if 0 <= d_x2 < 2001 and 0 <= d_y2 < 2001:  # 우하 그리고 왼쪾으로 움직이는 것 찾아라
                    if maps[d_x2][d_y2] != 0:
                        d_energy, d_direction = maps[d_x2][d_y2]
                        if d_direction == 3:
                            collisions.append([x, y, d_x2, d_y2, energy, d_energy])
                            flag = True
                if flag:
                    break


        if direction == 2: #나는 왼쪽방향 오른쪽 방향을 찾아라
            for dy in rows[x]:
                if dy != y and y < dy:
                    d_energy,d_direction = maps[x][dy]
                    if d_direction == 3:
                        collisions.append([x,y,dy,y,energy,d_energy,abs(x-dy)])
                        if min_dist > abs(y-dy):
                            min_dist = abs(y-dy)
            # min_dist 과 같거나 더 작은 좌상 좌하 존재하는가?
            flag = False
            for k in range(1,min_dist+1): #좌상 아래쪽 움직이는 것 찾아라
                d_x1,d_y1 = x-k,y-k #좌상
                d_x2,d_y2 = x-k,y+k #좌하
                if 0<= d_x1 < 2001 and 0<= d_y1 < 2001:
                    if maps[d_x1][d_y1] != 0:
                        d_energy, d_direction = maps[d_x1][d_y1]
                        if d_direction == 1:
                            collisions.append([x, y, d_x1, d_y1, energy, d_energy])
                            flag = True

                if 0<= d_x2 < 2001 and 0<= d_y2 < 2001: #좌하 위쪽으로 움직이는 것 찾아라
                    if maps[d_x2][d_y2] != 0:
                        d_energy, d_direction = maps[d_x2][d_y2]
                        if d_direction == 0:
                            collisions.append([x, y, d_x2, d_y2, energy, d_energy])
                            flag = True
                if flag:
                    break

        if direction == 3: #나는 오른쪽방향 왼쪽 방향을 찾아라
            for dy in rows[x]:
                if dy != y and y > dy:
                    d_energy,d_direction = maps[x][dy]
                    if d_direction == 2:
                        collisions.append([x,y,dy,y,energy,d_energy,abs(x-dy)])
                        if min_dist > abs(y-dy):
                            min_dist = abs(y-dy)
            # min_dist 과 같거나 더 작은 우상 우하 존재하는가?
            flag = False
            for k in range(1,min_dist+1): #우상 아래쪽 움직이는 것 찾아라
                d_x1,d_y1 = x+k,y-k #우상
                d_x2,d_y2 = x+k,y+k #우하
                if 0<= d_x1 < 2001 and 0<= d_y1 < 2001:
                    if maps[d_x1][d_y1] != 0:
                        d_energy, d_direction = maps[d_x1][d_y1]
                        if d_direction == 1:
                            collisions.append([x, y, d_x1, d_y1, energy, d_energy])
                            flag = True

                if 0<= d_x2 < 2001 and 0<= d_y2 < 2001: #우하 위쪽으로 움직이는 것 찾아라
                    if maps[d_x2][d_y2] != 0:
                        d_energy, d_direction = maps[d_x2][d_y2]
                        if d_direction == 0:
                            collisions.append([x, y, d_x2, d_y2, energy, d_energy])
                            flag = True
                if flag:
                    break
    print(collisions)

