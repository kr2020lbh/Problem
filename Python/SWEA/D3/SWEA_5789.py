#현주의 상자 바꾸기

#입력 받으면 순차적으로 인덱싱하여 그 배열의 위치에 숫자를 입력한다.
T = int(input())
for t in range(1,T+1):
    N,Q = map(int,input().split())
    boxes = [0] * N
    result = ' '
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        boxes[L-1:R] = [i]*(R-L+1)
    print(f'#{t}',end=' ')
    for n in range(N):
        print(boxes[n],end=' ')
    print()