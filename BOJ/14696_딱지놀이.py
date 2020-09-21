import sys
sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline())
for _ in range(N):
    a = [0]*4; b = [0]*4

    A = list(map(int,sys.stdin.readline().split()))
    B = list(map(int,sys.stdin.readline().split()))

    for i in range(1,A[0]+1):
        a[A[i]-1]+=1
    for i in range(1,B[0]+1):
        b[B[i]-1]+=1

    for i in range(3,-1,-1):
        if a[i] > b[i]:
            print('A')
            break
        if a[i] < b[i]:
            print('B')
            break
    else:
        print('D')
