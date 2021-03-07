delta = {
    'U' : [-1,0],
    'L' : [0,-1],
    'D' : [1,0],
    'R' : [0,1],
}
def solution(dirs):
    dirs = list(dirs)
    i,j = [5,5]
    visited = []
    maps = [[0]*11 for _ in range(11)]
    answer = 0
    for dir in dirs:
        di,dj = delta[dir]
        d_i = i + di
        d_j = j + dj
        if 0<= d_i < 11 and 0<= d_j < 11:
            if not [i,j,d_i,d_j] in visited:
                answer += 1
                visited.append([i,j,d_i,d_j])
                visited.append([d_i,d_j,i,j])
            i = d_i
            j = d_j
    return answer


solution('ULURRDLLU')