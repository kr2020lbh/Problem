import sys
sys.stdin = open("input.txt","r")

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
def bfs():

    Q = list()
    Q.append([0,0])
    ans[0][0]=0

    while Q:
        row,col = Q.pop(0)
        [print(a) for a in ans]

        for i in range(4):
            dr = row + d_row[i]
            dc = col + d_col[i]
            if 0<= dr <N and 0<= dc <N:
                dist = 0
                if arr[dr][dc]!=0:
                    dist +=arr[dr][dc]

                if ans[dr][dc] > ans[row][col]+dist :
                    ans[dr][dc] = ans[row][col]+dist
                    Q.append([dr,dc])



for t in range(1,int(input())+1):
    N = int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    ans=[[11111]*N for _ in range(N)]
    bfs()
    print("#{} {}".format(t,ans[-1][-1]))