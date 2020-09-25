#기차 사이의 파리


# 거리와 속도를 통해 쉽게 계산할 수있다.
# A와 B 기차의 속도를 통해서 주행 시간을 구하고, 파리의 속도만 곱하면 된다.
T = int(input())
for t in range(1,T+1):
    D,A,B,F = map(int,input().split())
    result = (D/(A+B))*F
    print(f'#{t} {result}')