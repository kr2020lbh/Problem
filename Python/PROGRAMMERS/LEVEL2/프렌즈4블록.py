def check_square(m,n,board):

    delete_indexes = [[False] * m for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == 'x':
                continue
            if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                delete_indexes[i][j] = True
                delete_indexes[i][j+1] = True
                delete_indexes[i+1][j] = True
                delete_indexes[i+1][j+1] = True
    return delete_indexes


def change_element(m,n,indexes,board):
    count = 0
    for i in range(n):
        idx = 0
        for j in range(m):
            if indexes[i][j]:
                del board[i][j-idx]
                board[i].append('x')
                idx += 1
                count += 1
    print(count)
    [print(b) for b in board]
    return count,board


def solution(m, n, board):
    new_board = []
    for a in list(zip(*board)):
        new_board.append(list(a)[::-1])
    [print(b) for b in new_board]

    answer = 0
    while True:
        indexes = check_square(m, n, new_board)
        count, new_board = change_element(m,n,indexes,new_board)
        if count:
            answer += count
        else:
            return answer

solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF'])
# solution(6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'])