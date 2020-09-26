import sys
sys.stdin = open("input.txt","r")
from itertools import permutations
import copy

#
# def get_row_sum_after_rotation(r,c,s):
#     for i in range(r-s,r+s+1):
#         if i == r-s:
#             row_sum_tmp[i] += arr[i+1][c-s]-arr[i][c+s]
#         elif i == r+s:
#             row_sum_tmp[i] += -arr[i][c-s]+arr[i-1][c+s]
#         else:
#             row_sum_tmp[i] += -(arr[i][c-s]+arr[i][c+s])+(arr[i+1][c-s]+arr[i-1][c+s])

# N,M,K = map(int,input().split())
# row_sum = []
# arr = []
#
# for i in range(N):
#     row = list(map(int,input().split()))
#     arr.append(row)
#     row_sum.append(sum(row))
#
# commands = [list(map(int,input().split())) for _ in range(K)]
# MIN = 5000
#
# for perm in permutations(range(K),K):
#     row_sum_tmp = row_sum[::]
#
#     for p in perm:
#         r,c,s = commands[p]
#         get_row_sum_after_rotation(r-1,c-1,s)
#     tmp = min(row_sum_tmp)
#     if tmp<MIN:
#         MIN = tmp

def get_sum(points):

    MIN = 500000
    for i in range(N):
        row_sum = 0
        for j in range(M):
            r,c = points[i][j]
            row_sum+=arr[r][c]
        if MIN > row_sum:
            MIN = row_sum
    return MIN

def rot(r,c,s):

    for k in range(s,0,-1):

        r_start = r-k
        r_end = r+k
        c_start = c-k
        c_end = c+k

        #왼쪽 상단과 우측 하단을 미리 복사
        left_top = tmp_point[r_start][c_start]
        right_bottom = tmp_point[r_end][c_end]

        #행 먼저 수행한다.
        #젤 왼쪽 열의 행, 자기 자신은 밑으로부터 온다
        #젤 오른쪽 열의 행 자기 자신은 위로부터 온다.
        for i in range(2*k):
            tmp_point[r_start+i][c_start] = tmp_point[r_start+i+1][c_start]
            tmp_point[r_end-i][c_end] = tmp_point[r_end-i-1][c_end]

        #열 수행
        #젤 위 행의 열, 자기 자신은 왼쪽으로 부터 온다
        #젤 아래 행의 열, 자기 자신은 오른쪽으로부터 온다
        for i in range(2*k-1):
            tmp_point[r_start][c_end-i] = tmp_point[r_start][c_end-i-1]
            tmp_point[r_end][c_start+i] = tmp_point[r_end][c_start+i+1]

        tmp_point[r_start][c_start+1] = left_top
        tmp_point[r_end][c_end-1] = right_bottom


N,M,K = map(int,input().split())
arr = []
arr_point = []
for i in range(N):
    arr_point.append([])
    row = list(map(int,input().split()))
    arr.append(row)
    for j in range(M):
        arr_point[-1].append([i,j])

commands = [list(map(int,input().split())) for _ in range(K)]

ans = 500000
for perm in permutations(range(K),K):
    tmp_point =copy.deepcopy(arr_point)
    for p in perm:
        r,c,s = commands[p]
        rot(r - 1, c - 1, s)

    res = get_sum(tmp_point)
    if res < ans:
        ans = res
print(ans)
