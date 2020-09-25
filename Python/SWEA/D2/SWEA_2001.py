#파리 퇴치
import sys
sys.stdin = open("input.txt","r")
def M(arr, n, m):
    MAX = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flies = 0
            for k in range(m):
                flies += sum(arr[i + k][j:j + m])
            if MAX < flies:
                MAX = flies
    return MAX

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr=[ list(map(int, input().split())) for _ in range(n)]
    print(f'#{t} {M(arr, n, m)}')