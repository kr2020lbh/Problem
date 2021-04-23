import sys
sys.stdin = open("input.txt","r")

from itertools import  product
def bfs(r,c,d):
    indexes = []
    visited = [[0]*10 for _ in range(10)]
    visited[r][c] = 1
    Q = [[r,c,0]]
    while Q:
        _r,_c,cnt = Q.pop(0)
        if cnt > d:
            continue
        indexes.append([_r,_c])
        for i in range(4):
            _dr,_dc = _r + dr[i], _c + dc[i]
            if _dr < 0 or _dr >= 10 or _dc < 0 or _dc >= 10:
                continue
            if visited[_dr][_dc] == 0:
                Q.append([_dr,_dc,cnt + 1])
                visited[_dr][_dc] = 1
    return indexes


def get_charge():
    global p1_charge,p2_charge
    points1 = maps[loc1[0]][loc1[1]]
    points2 = maps[loc2[0]][loc2[1]]
    if not points1 or not points2:
        max_point = 0
        if not points1:
            for point in points2:
                r,c = point
                max_point = max(max_point,bc[(r,c)][0])
            p2_charge += max_point
        if not points2:
            for point in points1:
                r,c = point
                max_point = max(max_point,bc[(r,c)][0])
            p1_charge += max_point
    else:
        max_point1 = 0
        max_point2 = 0
        max_point = 0
        for pd in list(product(points1,points2)):
            r1,c1 = pd[0]
            r2,c2 = pd[1]

            bc[(r1, c1)][1] += 1
            bc[(r2, c2)][1] += 1
            if max_point < bc[(r1, c1)][0]//bc[(r1, c1)][1] + bc[(r2, c2)][0]//bc[(r2, c2)][1]:
                max_point = bc[(r1, c1)][0]//bc[(r1, c1)][1] + bc[(r2, c2)][0]//bc[(r2, c2)][1]
                max_point1 = bc[(r1, c1)][0]//bc[(r1, c1)][1]
                max_point2 = bc[(r2, c2)][0]//bc[(r2, c2)][1]
            bc[(r1,c1)][1] = 0
            bc[(r2,c2)][1] = 0
        p1_charge += max_point1
        p2_charge += max_point2

dr = [-1,0,1,0]
dc = [0,1,0,-1]
T = int(input())
for tc in range(1,T+1):
    M,A = map(int,input().split()) #이동시간, 충전소 수
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    maps = [[[] for _ in range(10)] for _ in range(10)]
    bc = {}
    p1_charge = 0
    p2_charge = 0
    for _ in range(A):
        c,r,d,p = map(int,input().split())
        bc[(r-1,c-1)] = [p,0]
        for mc,mr in bfs(r-1,c-1,d):
            maps[mc][mr].append([r-1,c-1])

    loc1 = [0,0]
    loc2 = [9,9]
    get_charge()
    for i in range(M):
        if p1[i]:
            loc1[0] += dr[p1[i]-1]
            loc1[1] += dc[p1[i]-1]
        if p2[i]:
            loc2[0] += dr[p2[i]-1]
            loc2[1] += dc[p2[i]-1]
        get_charge()
    print("#{} {}".format(tc,p1_charge+p2_charge))