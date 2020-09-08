def f(r,c):
    Q = []
    Q.append([r,c])
    cnt=1
    while Q:
        tmp = Q.pop(0)
        r,c = tmp[0],tmp[1]
        num = arr[r][c]
        for i in range(4):
            dr = r + d_r[i]
            dc = c + d_c[i]
            if 0<= dr < N and 0<= dc < N and (arr[dr][dc]-num) == 1:
                Q.append([dr,dc])
                cnt+=1
    return cnt


d_r = [-1,1,0,0]
d_c = [0,0,-1,1]
for t in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    MAX = 0
    numbers = []
    for r in range(N):
        for c in range(N):
            if MAX > N**2-arr[r][c]:
                continue
            count = f(r,c)
            if MAX <= count:
                MAX = count
                numbers.append([MAX,arr[r][c]])
    numbers.sort(key=lambda x:(-x[0],x[1]))
    print("#{} {} {}".format(t,numbers[0][1],numbers[0][0]))