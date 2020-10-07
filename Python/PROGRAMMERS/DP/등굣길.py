def solution(m, n, puddles):
    row = n
    col = m
    arr = [ [ [0,0] for _ in range(col) ] for _ in range(row)]

    for puddle in puddles:
        arr[puddle[1]-1][puddle[0]-1][0] = 0
        arr[puddle[1]-1][puddle[0]-1][1] = 1

    for i in range(col):
        if arr[0][i][1] == 1:
            break
        arr[0][i][0] = 1
    for i in range(row):
        if arr[i][0][1] == 1:
            break
        arr[i][0][0] = 1


    for i in range(1,row):
        for j in range(1,col):
            if arr[i][j][1]==0:
                arr[i][j][0]=arr[i-1][j][0]+arr[i][j-1][0]

    return arr[row-1][col-1][0]%1000000007



print(solution(4,3,[[2, 2]]))