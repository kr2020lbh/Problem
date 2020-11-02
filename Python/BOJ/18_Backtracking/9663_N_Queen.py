def check(row):
    global cnt
    if row == N:
        cnt += 1
    else:
        for col in range(N):
            if a[col] == False and b[row+col]==False and c[row-col+N-1]==False:
                a[col] = b[row+col] = c[row-col+N-1] = True
                check(row+1)
                a[col] = b[row+col] = c[row-col+N-1] = False

N=int(input())
a,b,c = [False]*N,[False]*(2*N-1),[False]*(2*N-1)
cnt = 0
check(0)
print(cnt)