def recur(point,length):
    x,y = point
    if length == 1:
        res[x][y] = '*'
    else:
        cnt = 0
        for i in range(0,length,length//3):
            for j in range(0,length,length//3):
                cnt+=1
                if cnt == 5: continue
                recur([x+i,y+j],length//3)

n = int(input())
res = [[' ']*n for _ in range(n)]
recur([0,0],n)
[print(''.join(r)) for r in res]