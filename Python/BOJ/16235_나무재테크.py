import sys
sys.stdin = open("input.txt","r")
def one_year():
    global  ans
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                temp = dict()
                die = 0
                for year,tree_cnt in sorted(tree[i][j].items()): #key는 나이, value는 나무 수
                    if land[i][j] >= tree_cnt * year: #양분이 충분
                        land[i][j] -= tree_cnt * year
                        temp[year+1] = tree_cnt
                    else: #양분 부족
                        survive = land[i][j] // year
                        if survive == 0:
                            die += (year//2) * tree_cnt
                        else:
                            die += (year//2) * (tree_cnt - survive)
                            land[i][j] -= (survive * year)
                            temp[year+1] = survive
                        ans -= (tree_cnt - survive)
                land[i][j] += die
                tree[i][j] = temp

    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree_res = 0
                for year,tree_cnt in tree[i][j].items():
                    if year % 5 == 0:
                        tree_res += tree_cnt
                if tree_res:
                    for d_i, d_j in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                        di = i + d_i
                        dj = j + d_j
                        if 0 <= di < N and 0 <= dj < N:
                            if tree[di][dj].get(1):
                                tree[di][dj][1] += tree_res
                            else:
                                tree[di][dj][1] = tree_res
                            ans += tree_res

    for i in range(N):
        for j in range(N):
            land[i][j] += val[i][j]


N,M,K = map(int,input().split())
val = [list(map(int,input().split())) for _ in range(N)]
land = [[5]*N for _ in range(N)]
tree = [[ dict() for _ in range(N)] for _ in range(N)]
ans = 0

for _ in range(M):
    x,y,year = map(int,input().split())
    if tree[x-1][y-1].get(year):
        tree[x-1][y-1][year]+=1
    else:
        tree[x-1][y-1][year]=1
    ans += 1

for _ in range(K):
    one_year()
print(ans)
