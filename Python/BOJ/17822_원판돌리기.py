import sys
sys.stdin = open("input.txt","r")

def rot(i,d,k):
    #i번째 원판
    if d == 0: #시계방향
        disks[i] = disks[i][M-k:M] + disks[i][0:M-k]
    if d == 1: #반시계방향
        disks[i] = disks[i][k:M] + disks[i][0:k]

def delete_adjacency():
    disk_sum = 0
    disk_cnt = 0
    indexes = set()
    for r in range(N):
        for c in range(M):
            me = disks[r][c]
            if me == -1:
                continue
            disk_sum += me
            disk_cnt += 1
            if r == 0:
                #같은 원판 내에서 인접한 수
                if me == disks[r][(c-1)%M]:
                    indexes.add((r,c))
                    indexes.add((r,(c-1)%M))
                if me == disks[r][(c+1)%M]:
                    indexes.add((r,c))
                    indexes.add((r,(c+1)%M))
                #다른 원판에서 인접한 수
                if me == disks[r+1][c]:
                    indexes.add((r,c))
                    indexes.add((r+1,c))
            elif r == N-1:
                #같은 원판 내에서 인접한 수
                if me == disks[r][(c-1)%M]:
                    indexes.add((r,c))
                    indexes.add((r,(c-1)%M))
                if me == disks[r][(c+1)%M]:
                    indexes.add((r,c))
                    indexes.add((r,(c+1)%M))
                #다른 원판에서 인접한 수
                if me == disks[r-1][c]:
                    indexes.add((r,c))
                    indexes.add((r-1,c))
            else:
                #같은 원판 내에서 인접한 수
                if me == disks[r][(c-1)%M]:
                    indexes.add((r,c))
                    indexes.add((r,(c-1)%M))
                if me == disks[r][(c+1)%M]:
                    indexes.add((r,c))
                    indexes.add((r,(c+1)%M))
                #다른 원판에서 인접한 수
                if me == disks[r-1][c]:
                    indexes.add((r,c))
                    indexes.add((r-1,c))
                if me == disks[r+1][c]:
                    indexes.add((r,c))
                    indexes.add((r+1,c))
    if indexes:
        for r,c in indexes:
            disks[r][c] = -1
    else:
        if disk_cnt != 0:
            disk_mean = disk_sum/disk_cnt

            for r in range(N):
                for c in range(M):
                    me = disks[r][c]
                    if me != -1:
                        if me > disk_mean:
                            disks[r][c] -= 1
                        elif me < disk_mean:
                            disks[r][c] += 1


N,M,T = map(int,input().split()) #N개의 원판 M개의 수 T번
disks = [list(map(int,input().split())) for _ in range(N)]
commands = [list(map(int,input().split())) for _ in range(T)] #X 배수 원판 D 방향 K 칸 회전
for X,D,K in commands:
    for x in range(N):
        if (x+1)%X == 0:
            rot(x,D,K)
    delete_adjacency()
ans = 0
for r in range(N):
    for c in range(M):
        if disks[r][c] != -1:
            ans += disks[r][c]
print(ans)