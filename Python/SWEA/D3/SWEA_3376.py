#파도반 수열
import sys
sys.stdin = open("input.txt","r")

result = []
for t in range(1,int(input())+1):
    base= [1, 1, 1, 2, 2]
    N = int(input())
    for i in range(5,N):
        base.append( base[i-1]+base[i-5] )
    result.append(f'#{t} {base[N-1]}')
print('\n'.join(result))
