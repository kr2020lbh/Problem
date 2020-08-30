import sys
sys.stdin = open("input.txt","r")

#board 4X4, 6X6, 8X8
#주변을 탐색하는 리스트
#시계방향 상 우상 우 우하 하 좌하 좌 좌상
delta_i = [-1,-1,0,1,1,1,0,-1]
delta_j = [0,1,1,1,0,-1,-1,-1]

def board_set():
    w_row,w_col = N//2-1,N//2-1
    b_row,b_col = N//2,N//2-1
    for i in range(2):
        board[w_row][w_col] = 2
        board[b_row][b_col] = 1
        w_row+=1;w_col+=1
        b_row-=1;b_col+=1

def check_around(r,c,mode):
    i = r; j = c
    d_i = i + delta_i[mode]
    d_j = j + delta_j[mode]
    if 0<= d_i <N and 0<=d_j<N and board[d_i][d_j]!=0:
        if board[d_i][d_j] != color:
            check_around(d_i,d_j,mode)
        else:
            change_color(row,col,d_i,d_j,mode)

#돌은 둔 곳 board[init_r][init_c]와
#탐색해서 끝낸 곳 board[r][c] 사이의 돌 색을 바꾸는 함수

def change_color(init_r,init_c,r,c,mode):
    cnt = max(abs(init_c-c),abs(init_r-r))
    change_row = init_r + delta_i[mode]
    change_col = init_c + delta_j[mode]
    while cnt>0:
        board[change_row][change_col] = color
        change_row+=delta_i[mode]
        change_col+=delta_j[mode]
        cnt-=1

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    board = [[0]*N for _ in range(N)]
    board_set()

    #각 돌을 두는 단계마다 주변에 뭐가 있는지 확인해야한다. 상하좌우 대각선
    #각 돌 옆에 반대되는 색상이 있고 그 다음 다시 자기 색이 나올때까지 탐색해서
    #사이에 있는 반대되는 색상의 돌을 자기 색으로 바꾼다.
    for i in range(M):
        col,row,color = map(int,input().split())
        row-=1;col-=1
        board[row][col] = color

        for mode in range(8):
            check_around(row,col,mode)

    white = 0
    black = 0
    for line in board:
        for stone in line:
            if stone == 1:
                black+=1
            elif stone == 2:
                white+=1
    print('#{} {} {}'.format(t,black,white))


