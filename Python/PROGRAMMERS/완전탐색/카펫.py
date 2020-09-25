def solution(brown, yellow):
    tiles = brown+yellow
    N=tiles//3
    while True:
        M = tiles//N
        if N*M == tiles and (N-2)*(M-2)==yellow:
            break
        N-=1
    answer = [N,M]
    return answer

solution(10,2)