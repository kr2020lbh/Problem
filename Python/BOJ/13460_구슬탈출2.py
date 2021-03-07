import sys
sys.stdin = open("input.txt")

def gravity(d):
    res = [0,0]
    if d==0: #위로 올리기
        for j in range(M):
            for i in range(N):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    me = maps[i][j]
                    row = i
                    while True:
                        if maps[row-1][j] == '.':
                            row -= 1
                        else:
                            if row == i:
                                if me == 'R':
                                    res[0] = -1
                                else:
                                    res[1] = -1
                                
                            if maps[row-1][j] == 'O':
                                maps[i][j] = '.'

                            elif maps[row-1][j] == '#':
                                maps[i][j] = '.'
                                maps[row][j] = me
                                
                            break

    if d==1: #아래로 내리기
        for j in range(M):
            for i in range(N-1,-1,-1):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    me = maps[i][j]
                    row = i
                    while True:
                        if maps[row+1][j] == '.':
                            row += 1
                        else:
                            if row == i:
                                if me == 'R':
                                    res[0] = -1
                                else:
                                    res[1] = -1

                            if maps[row+1][j] == 'O':
                                maps[i][j] = '.'

                            elif maps[row+1][j] == '#':
                                maps[i][j] = '.'
                                maps[row][j] = me
                            break
    
    if d==2: #왼쪽으로 기울이기
        for i in range(N):
            for j in range(M):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    me = maps[i][j]
                    col = j
                    while True:
                        if maps[i][col-1] == '.':
                            col -= 1
                        else:
                            if col == j:
                                if me == 'R':
                                    res[0] = -1
                                else:
                                    res[1] = -1
                                
                            if maps[i][col-1] == 'O':
                                maps[i][j] = '.'

                            elif maps[i][col-1] == '#':
                                maps[i][j] = '.'
                                maps[i][col] = me
                            break
    
    if d==3: #오른쪽으로 기울이기
        for i in range(N):
            for j in range(M-1,-1,-1):
                if maps[i][j] == 'R' or maps[i][j] == 'B':
                    me = maps[i][j]
                    col = j
                    while True:
                        if maps[i][col+1] == '.':
                            col += 1
                        else:
                            if col == j:
                                if me == 'R':
                                    res[0] = -1
                                else:
                                    res[1] = -1

                            if maps[i][col+1] == 'O':
                                maps[i][j] = '.'

                            elif maps[i][col+1] == '#':
                                maps[i][j] = '.'
                                maps[i][col] = me
                            break
    print_maps(d)
    print(res)
def print_maps(d):
    if d==0:
        print('위로 기울이기')
    elif d==1:
        print('아래로 기울이기')
    elif d==2:
        print('왼쪽으로 기울이기')
    elif d==3:
        print('오른쪽으로 기울이기')
    else:
        print('초기')
    [print(m) for m in maps]
N,M = map(int,input().split())
maps = [list(input()) for _ in range(N)]
print_maps(-1)
gravity(3)
gravity(1)
gravity(2)
gravity(0)



                        

