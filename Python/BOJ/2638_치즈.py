import sys
sys.stdin = open("input.txt","r")

def bfs():
    visited = [[0]*M for _ in range(N)]
    Q = [[0,0]]
    cheeses = dict()
    points = []
    while Q:
        r,c = Q.pop(0)
        for i in range(4):
            _dr = r + dr[i]
            _dc = c + dc[i]
            if 0<= _dr < N and 0<= _dc < M:
                if maps[_dr][_dc] == 0:
                    if visited[_dr][_dc] == 0:
                        visited[_dr][_dc] = 1
                        Q.append([_dr, _dc])
                else:
                    if cheeses.get((_dr,_dc)):
                        cheeses[(_dr, _dc)] += 1
                        if cheeses[(_dr, _dc)] == 2:
                            points.append([_dr,_dc])

                    else:
                        cheeses[(_dr, _dc)] = 1
    if points:
        for r,c in points:
            maps[r][c] = 0
        return True
    else:
        return False

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
res = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
while bfs():res += 1
print(res)

