#어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open('input.txt','r')
# find_row 함수는 행에서 단어가 들어갈 수 있는곳 찾기
# N*N 행렬
# index 0인  열에서는 1이 K개 나오고 0이 K+1 번째  나와야한다
# index 마지막 열에서는 1이 K개 나오고 N-1-K 번째 열이 0
# 나머지는 0 1 1 1 1 ...(K개) 0
# find_col 함수는 입력된 행렬을 90도 시계방향 회전 후 find_row 함수 호출
def find_row(arr,K):
    count = 0
    for i in range(N):
        if sum(arr[i][0:K]) == K and arr[i][K] == 0:
            count += 1
        if sum(arr[i][N-K:N])==K and arr[i][N-K-1]==0:
            count += 1
        for j in range(1,N-K):
            if sum(arr[i][j:j+K]) == K and arr[i][j-1]==0 and arr[i][j+K]==0:
                count+=1
    return count

def find_col(arr,K):
    rot_arr = [ [0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot_arr[i][j]=arr[N-1-j][i]
    return find_row(rot_arr,K)

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = [ list(map(int,input().split())) for _ in range(N)]
    print(f'#{t} {find_row(arr,K)+find_col(arr,K)}')