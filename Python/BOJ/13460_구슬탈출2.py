import sys
sys.stdin = open("input.txt")

def printMaps():
    print("print Maps")
    [print(m) for m in maps]

def dfs(depth):
    if depth > MIN_DEPTH:
        return
    for i in range(4):
        gravity(i)

def move(r,c,d,HOLE,color):
    nr,nc = r,c
    if d == 0:
        while True:
            if maps[nr-1][nc] == '.':
                nr -= 1
            else:
                if maps[nr-1][nc] == 'O':
                    HOLE[color] = True
                break

def gravity(d):
    HOLE = [False,False]
    Rrow,Rcol = indexes[0]
    Brow,Bcol = indexes[1]
    #상우하좌
    if d == 0: #상
        if Rcol == Bcol:
            if Rrow < Brow:
                pass
            else:
                pass

        else:
            pass

    elif d == 1: #우
        if Rrow == Rrow:
            pass
        else:
            pass

    elif d == 2: #하
        if Rcol == Bcol:
            pass
        else:
            pass

    elif d == 3: #좌
        if Rrow == Brow:
            pass
        else:
            pass



DELTA = [[-1,0],[0,1],[1,0],[0,-1]]
MIN_DEPTH = 10
N,M = map(int,input().split())
maps = []
indexes = [0,0] #R,B
for r in range(N):
    row = list(input())
    for c in range(M):
        if row[c] == 'R':
            indexes[0] = [r,c]
        elif row[c] == 'B':
            indexes[1] = [r,c]
    maps.append(row)


