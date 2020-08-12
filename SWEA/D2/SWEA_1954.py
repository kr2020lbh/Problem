#달팽이 숫자
import sys
sys.stdin = open("input.txt","r")
modes = [(0,1), (1,0),(0,-1),(-1,0)]
def snail():
    count = 1
    mode = 0
    start_row=start_col=0
    end_row=end_col=N-1
    i=j=0
    while count <= N**2:
        arr[i][j]=count
        if mode == 0:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if j == end_col:
                mode+=1
                start_row+=1
        elif mode == 1:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if i == end_row:
                mode+=1
                end_col-=1
        elif mode == 2:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if j == start_col:
                mode+=1
                end_row-=1
        else:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if i == start_row:
                mode+=1
                start_col+=1
        count+=1
        mode%=4
for t in range(1,int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    snail()
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()
