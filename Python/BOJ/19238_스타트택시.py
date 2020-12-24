import sys
sys.stdin = open("input.txt","r")


def find_passenger(tr,tc):
    global GAS
    Q = [[tr,tc,1]]
    tmp_passengers = []
    visited = [[0]*N for _ in range(N)]
    if maps[tr][tc] == -1:
        tmp_passengers.append([tr, tc, 0])
    visited[tr][tc] = 1
    while Q:
        r,c,distance = Q.pop(0)
        for i in range(4):
            d_r = r + dr[i]
            d_c = c + dc[i]
            if 0<= d_r < N and 0<= d_c < N and maps[d_r][d_c] != 1 and visited[d_r][d_c] == 0:
                visited[d_r][d_c] = 1
                if maps[d_r][d_c] == -1:
                    tmp_passengers.append([d_r,d_c,distance])
                Q.append([d_r,d_c,distance+1])

    if len(tmp_passengers) == 0:
        return False
    tmp_passengers.sort(key=lambda x:(x[2],x[0],x[1]))
    sr,sc,distance = tmp_passengers[0]
    er,ec = destinations[sr][sc]
    Q = [[sr,sc,0]]
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1
    flag = False
    while Q:
        r,c,ride_distance = Q.pop(0)
        if r == er and c == ec:
            flag = True
            break
        for i in range(4):
            d_r = r + dr[i]
            d_c = c + dc[i]
            if 0<= d_r < N and 0<= d_c < N and maps[d_r][d_c] != 1 and visited[d_r][d_c] == 0:
                visited[d_r][d_c] = 1
                Q.append([d_r,d_c,ride_distance+1])
    if flag == False:
        return False
    total_distance = distance + ride_distance
    if GAS < total_distance:
        return False
    else:
        maps[sr][sc] = 0
        GAS = GAS - distance + ride_distance
        return er,ec


N,M,GAS = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
destinations = [[ [] for _ in range(N) ] for _ in range(N)]
tr,tc = map(int,input().split())
tr -=1 ; tc -= 1
passengers = []
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for _ in range(M):
    sr,sc,er,ec = map(int,input().split())
    sr -= 1; sc -=1 ; er -=1; ec -= 1
    destinations[sr][sc] = [er,ec]
    maps[sr][sc] = -1


for _ in range(M):
    res = find_passenger(tr, tc)
    if res == False:
        print(-1)
        break
    else:
        tr,tc = res
else:
    print(GAS)
