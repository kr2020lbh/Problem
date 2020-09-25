#세제곱근을 찾아라
#수를 입력받아 3제곱근으로 만들어 6 번째 자리에서 반올림 한 수가 
# X.0 으로 딱 떨어지면 그 수는 3제곱근이다.
#이를 확인하기 위해서 str(N)[-2] 가  '.' 인지 확인한다.
for t in range(int(input())):
    N = int(input())
    x = round(N**(1/3),6)
    x = int(x) if str(x)[-2]=='.' else -1
    print(f'#{t+1} {x}')