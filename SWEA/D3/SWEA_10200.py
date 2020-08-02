#둘 다 만족하는 수를 구하는데
#최대 : 둘 중 작거나 같은 것
#최소 : A+B가 N보다 작으면 0, 아니면 N-(A+B)

T = int(input())
for t in range(T):
    N,A,B = map(int,input().split())
    MAX=min(A,B)
    MIN=(0 if (A+B)<N else (A+B-N))
    print(f'#{t+1} {MAX} {MIN}')