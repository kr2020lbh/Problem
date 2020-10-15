def solution(n):
    snail = [[0]*i for i in range(1,n+1)]
    col_move = [0,1,-1]
    row_move = [1,0,-1]
    cnt = 1
    move = row = col = 0

    while cnt <= n*(n+1)//2:
        snail[row][col] = cnt
        cnt+=1
        if 0 <= row + row_move[move] < n and 0 <= col + col_move[move] < n and snail[row + row_move[move]][col + col_move[move]] == 0:
            pass
        else:
            move = (move+1)%3
        row += row_move[move]
        col += col_move[move]

    answer = []
    for s in snail:
        answer += s
    return answer
