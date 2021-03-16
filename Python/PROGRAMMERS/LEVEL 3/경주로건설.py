from copy import deepcopy
moves = [[-1,0],[1,0],[0,-1],[0,1]]
ans = 10**8

def next_move(board,r,c,move,turn,prev_d):
    N = len(board)

    global ans
    if ans < move * 100 + 500 * turn:
        return

    if r == N-1 and c == N-1:
        print("move : {} turn : {} cost : {}".format(move, turn,move * 100 + turn * 500))
        [print(b) for b in board]
        tmp_ans = move * 100 + turn * 500
        if tmp_ans < ans:
            ans = tmp_ans
        return


    board[r][c] = 1
    for i in range(4):
        dr, dc = moves[i]
        nr,nc = r+dr,c+dc
        if 0<= nr < N and 0<= nc < N and board[nr][nc] == 0:
            tmp_board = deepcopy(board)
            tmp_board[nr][nc] = 1
            if i != prev_d:
                next_move(tmp_board,nr,nc,move+1,turn+1,i)
            else:
                next_move(tmp_board,nr,nc,move+1,turn,i)


def solution(board):
    N = len(board)
    r,c = 0,0
    board[r][c] = 1
    for i in range(4):
        dr, dc = moves[i]
        nr,nc = r+dr,c+dc
        if 0<= nr < N and 0<= nc < N and board[nr][nc] == 0:
            tmp_board = deepcopy(board)
            tmp_board[nr][nc] = 1
            next_move(tmp_board,nr,nc,1,0,i)
    return ans
    # return answer

solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	)