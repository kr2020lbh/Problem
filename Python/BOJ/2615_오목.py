import sys
sys.stdin = open("input.txt","r")

def check(i,j,me):
    #세로 오목
    if 0 < i < 14:
        if board[i-1][j] != me and board[i+5][j] != me:
            for r in range(5):
                if board[i+r][j] != me:
                    break
            else:
                return True
    elif i == 0:
        if board[i+5][j] != me:
            for r in range(5):
                if board[i+r][j] != me:
                    break
            else:
                return True
    elif i == 14:
        if board[i-1][j] != me:
            for r in range(5):
                if board[i+r][j] != me:
                    break
            else:
                return True
    #가로 오목
    if 0 < j < 14:
        if board[i][j-1] != me and board[i][j+5] != me:
            for c in range(5):
                if board[i][j+c] != me:
                    break
            else:
                return True
    elif j == 0:
        if board[i][j+5] != me:
            for c in range(5):
                if board[i][j+c] != me:
                    break
            else:
                return True
    elif j == 14:
        if board[i][j-1] != me:
            for c in range(5):
                if board[i][j+c] != me:
                    break
            else:
                return True
    #우상단 대각 오목
    if 4 < i <18 :
        if  0 < j < 14:
            if board[i + 1][j - 1] != me and board[i - 5][j + 5] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True
        if j == 0:
            if board[i - 5][j + 5] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True
        if j == 14:
            if board[i + 1][j - 1] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True

    elif i == 4:
        if  0 < j < 14:
            if board[i + 1][j - 1] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True
        if j == 0:
            for k in range(5):
                if board[i - k][j + k] != me:
                    break
            else:
                return True
        if j == 14:
            if board[i + 1][j - 1] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True
    elif i == 18:
        if  0 < j < 14:
            if board[i - 5][j + 5] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True
        if j == 0:
            if board[i - 5][j + 5] != me:
                for k in range(5):
                    if board[i - k][j + k] != me:
                        break
                else:
                    return True
        if j == 14:
            for k in range(5):
                if board[i - k][j + k] != me:
                    break
            else:
                return True
    #우하단 대각 오목
    if 0 < i <14 :
        if  0 < j < 14:
            if board[i - 1][j - 1] != me and board[i + 5][j + 5] != me:
                for k in range(5):
                    if board[i + k][j + k] != me:
                        break
                else:
                    return True
        if j == 0:
            if board[i + 5][j + 5] != me:
                for k in range(5):
                    if board[i + k][j + k] != me:
                        break
                else:
                    return True
        if j == 14:
            if board[i - 1][j - 1] != me:
                for k in range(5):
                    if board[i + k][j + k] != me:
                        break
                else:
                    return True

    elif i == 0:
        if  0 <= j < 14:
            if board[i + 5][j + 5] != me:
                for k in range(5):
                    if board[i + k][j + k] != me:
                        break
                else:
                    return True

        if j == 14:
            for k in range(5):
                if board[i - k][j + k] != me:
                    break
            else:
                return True
    elif i == 14:
        if  0 < j <= 14:
            if board[i - 1][j - 1] != me:
                for k in range(5):
                    if board[i + k][j + k] != me:
                        break
                else:
                    return True
        if j == 0:
            for k in range(5):
                if board[i + k][j + k] != me:
                    break
            else:
                return True

def soulution():
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0: continue
            if check(i,j,board[i][j]):
                print(board[i][j])
                print(i+1,j+1)
                return
    print(0)
board = [list(map(int,input().split())) for _ in range(19)]
soulution()