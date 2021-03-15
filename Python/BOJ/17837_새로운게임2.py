import sys
sys.stdin = open("input.txt","r")

def change_d(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2

delta = [[0,1],[0,-1],[-1,0],[1,0]]
N,K = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
targets = []
for i in range(N):
    row = []
    for j in range(N):
        row.append([])
    targets.append(row)

orders = []
for _ in range(K):
    r,c,d = map(int,input().split())
    orders.append([r-1,c-1,_]) #행, 열, 말 번호
    targets[r-1][c-1].append([_,d-1])


cnt = 0

while cnt < 10:
    cnt += 1

    for i in range(K):
        print('-------#{}번 말 움직일 순서--------'.format(i))
        r,c,idx = orders[i] #행, 열, 말 번호
        print("행 : {}, 열 : {}, 말 번호 : {}".format(r,c,idx))
        target = targets[r][c]
        print("{}행{}열에 있는 말 들 : {}".format(r,c,targets[r][c]))
        for j in range(len(target)):
            if target[j] and target[j][0] == idx:
                break
        d = target[j][1]
        dr,dc = r + delta[d][0], c + delta[d][1]
        if 0<= dr < N and 0<= dc < N and maps[dr][dc] != 2:
            stay,move = target[:j],target[j:]
            target[j] = stay[::]
            if maps[dr][dc] == 0:#흰색인 경우
                targets[dr][dc].append(move)
            else:#빨간색인 경우
                targets[dr][dc].append(move[::-1])
            orders[i] = [dr,dc,idx]
        else: #파란색인 경우
            d = change_d(d)
            dr, dc = r + delta[d][0], c + delta[d][1]
            if 0 <= dr < N and 0 <= dc < N and maps[dr][dc] != 2:
                stay, move = target[:j], target[j:]
                target[j] = stay[::]
                if maps[dr][dc] == 0:  # 흰색인 경우
                    targets[dr][dc].append(move)
                else:  # 빨간색인 경우
                    targets[dr][dc].append(move[::-1])
                orders[i] = [dr, dc, idx]
            else:
                target[j][1] = d
        print('-------#{}번 말 움직이기 종료--------'.format(i))
        print()

