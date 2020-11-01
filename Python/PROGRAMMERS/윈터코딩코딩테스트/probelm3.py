dr = [-1,1,0,0]
dc = [0,0,-1,1]
def find(num,i,j,v,limit):
    Q = [[i,j]]
    while Q:
        row,col = Q.pop()
        for i in range(4):
            d_row = row + dr[i]
            d_col = col + dc[i]
            if 0<= d_row < limit and 0<= d_col <limit:
                if v[d_row][d_col] == num:
                    Q.append([d_row,d_col])
                    v[d_row][d_col] = -1
    return v


def solution(v):
    answer = [0,0,0]

    for num in range(3):
        for i in range(len(v)):
            for j in range(len(v)):
                if v[i][j] == num:
                    v = find(num,i,j,v,len(v))
                    answer[num] += 1
    return answer

solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]])