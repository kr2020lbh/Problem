#파스칼의 삼각형
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N = int(input())
    pascal = [ [0]*i for i in range(1,N+1)]
    print(f'#{t}')
    for i in range(N):
        pascal[i][0]=pascal[i][-1]=1
        if i>=2:
            for j in range(1,i):
                pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
        for num in pascal[i]:
            print(num,end=' ')
        print()

