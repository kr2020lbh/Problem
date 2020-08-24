import sys
sys.stdin = open("input.txt","r")

for t in range(int(input())):

    N,M = map(int,input().split())
    W = [0]*N
    B = [0]*N
    R = [0]*N
    flag = [input() for _ in range(N)]

    for idx,line in enumerate(flag):
        for element in line:
            if element != 'W':
                W[idx]+=1
            if element != 'B':
                B[idx]+=1
            if element != 'R':
                R[idx]+=1
        if idx != 0:
            W[idx]+=W[idx-1]
            B[idx] += B[idx - 1]
            R[idx] += R[idx - 1]
    MIN = N*M


    # i의 범위는 0부터 N-3
    # j의 범위는 i+1부터 N-2
    # k의 범위는 j+1부터 N-1


    for i in range(N-2):
        for j in range(i+1,N-1):
            SUM = W[i]+B[j]-B[i]+R[N-1]-R[j]
            if MIN>SUM:
                MIN = SUM
    print('#{} {}'.format(t+1,MIN))