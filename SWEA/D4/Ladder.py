import sys
sys.stdin = open("input.txt","r")
#2에서 시작해서 위로 올라간다
#move_up 중에는 좌우만 살핀다.
#좌우를 살피다 1이 나오면 move_side로 바뀐다.
#move_side 중에는 위만 살핀다
#위 칸에 1이 나오면 다시 move_up로 바뀐다.
#위에 0이 나오면 종료한다
def search_ladder(row,col):
    move_up = True
    move_side = False
    move = 0 #왼쪽 진행 중인지 오른쪽 진행 중인지
    while ladder[row][col] != 0:
        # print(row,col)
        if move_up:
            if ladder[row-1][col]==0:
                return col-1

            elif ladder[row][col+1] == 1: #오른쪽이 1이면 오른쪽으로 진행
                move_side = True
                move_up = False
                move = 1
                col+=1
            elif ladder[row][col-1] == 1: #왼쪽이 1이면 왼쪾으로 진행
                move_side = True
                move_up = False
                move = -1
                col-=1
            else:
                row-=1


        if move_side:
            if ladder[row-1][col]==1:
                move_up=True
                move_side=False
                row-=1
            elif move==1:
                col+=1
            elif move==-1:
                col-=1

for t in range(1,11):
    tc = int(input())
    ladder = [0]*101
    ladder[0] = [0]*102
    for i in range(1,101):
        ladder[i] = [0]+list(map(int,input().split()))+[0]
    for i in range(1,101):
        if ladder[-1][i]==2:
            end_idx = i
            break

    print('#{} {}'.format(tc,search_ladder(100,end_idx)))