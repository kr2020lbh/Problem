import sys
sys.stdin = open("input.txt","r")

def sum_fire(r,c):
    M=S=cnt=0
    D=[]
    for m,s,d in arr[r][c]:
        M += m
        S += s
        D.append(d%2)
        cnt+=1

    arr[r][c] = []

    if M // 5 == 0:return []

    if sum(D) == cnt or sum(D) == 0:
        for d in [0,2,4,6]:
            arr[r][c].append([M//5,S//cnt,d])
    else:
        for d in [1,3,5,7]:
            arr[r][c].append([M//5,S//cnt,d])



d_row = [-1,-1,0,1,1,1,0,-1]
d_col = [0,1,1,1,0,-1,-1,-1]
N,M,K = map(int,input().split())
arr = [[ [] for _ in range(N)] for _ in range(N)]
indexes = []

for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    arr[r-1][c-1].append([m,s,d])
    indexes.append([r-1,c-1])

for _ in range(K):
    tmp_index = []
    tmp_msd = []
    while indexes:
        r,c = indexes.pop()
        for _ in range(len(arr[r][c])):
            m,s,d = arr[r][c].pop()
            dr = (r + d_row[d] * s)%N
            dc = (c + d_col[d] * s)%N
            tmp_msd.append([dr,dc,m,s,d])

    for r,c,m,s,d in tmp_msd:
        tmp_index.append([r,c])
        arr[r][c].append([m,s,d])

    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) > 1:
                sum_fire(i,j)

    indexes = tmp_index[::]

res = 0
for i in range(N):
    for j in range(N):
        for m,s,d in arr[i][j]:
            res += m
print(res)


