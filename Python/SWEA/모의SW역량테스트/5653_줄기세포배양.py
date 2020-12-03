import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    CASE_LIMIT = 360
    case = [[0]*CASE_LIMIT for _ in range(CASE_LIMIT)]
    start_row = CASE_LIMIT//2-N//2
    start_col = CASE_LIMIT//2-M//2

    growing_times = [[0]*CASE_LIMIT for _ in range(CASE_LIMIT)]

    for i in range(N):
        row = list(map(int,input().split()))
        for j in range(M):
            if row[j] != 0:
                case[start_row+i][start_col+j] = row[j]

    time = 0
    while time < K:
        visited = [[0]*CASE_LIMIT for _ in range(CASE_LIMIT)]
        new_indexes = []
        for i in range(CASE_LIMIT):
            for j in range(CASE_LIMIT):
                ability = case[i][j]
                if ability != 0 and not visited[i][j]:
                    visited[i][j] = 1
                    growing_time = growing_times[i][j]
                    if ability <= growing_time < ability*2:
                        for d_i,d_j in [[-1,0],[0,1],[1,0],[0,-1]]:
                            di = i + d_i
                            dj = j + d_j
                            if case[di][dj] == 0:
                                new_indexes.append([di,dj,ability])
                    growing_times[i][j] += 1
        new_indexes.sort(key=lambda x:x[-1])
        for di,dj,ability in new_indexes:
            case[di][dj] = ability
        time += 1

    cnt = 0
    for i in range(CASE_LIMIT):
        for j in range(CASE_LIMIT):
            if case[i][j] != 0:
                if growing_times[i][j] < 2*case[i][j]:
                    cnt += 1
    print("#{} {}".format(t,cnt))