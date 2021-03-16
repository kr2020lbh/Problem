def get_cost(cost,new_d,cur_d):
    if (new_d == 'U' or new_d == 'D') and (cur_d == 'U' or cur_d == 'D'):
        return cost + 100
    if (new_d == 'U' or new_d == 'D') and (cur_d == 'L' or cur_d == 'R'):
        return cost + 600
    if (new_d == 'L' or new_d == 'R') and (cur_d == 'L' or cur_d == 'R'):
        return cost + 100
    if (new_d == 'L' or new_d == 'R') and (cur_d == 'U' or cur_d == 'D'):
        return cost + 600

def bfs(direction,board):
    N = len(board)
    directions = [[1,0,'D'],[-1,0,'U'],[0,1,'R'],[0,-1,'L']]
    Q = [[0,0,0,direction]] #r,c,cost,direction
    costs = [[0]*N for _ in range(N)]
    while Q:
        r,c,cost,cur_dir = Q.pop(0)
        for i in range(4):
            dr,dc,dd = directions[i]
            nr,nc = r+dr,c+dc
            new_cost = get_cost(cost,dd,cur_dir)
            if 0<= nr < N and 0<= nc < N and board[nr][nc] == 0:
                if costs[nr][nc] == 0 or costs[nr][nc] > new_cost:
                    costs[nr][nc] = new_cost
                    Q.append([nr,nc,new_cost,dd])
    return costs[N-1][N-1]

def solution(board):
    return min(bfs('R',board),bfs('D',board))
    

    # return answer

solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	)