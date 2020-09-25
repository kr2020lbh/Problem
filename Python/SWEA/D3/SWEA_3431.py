#준환이의 운동관리
import sys
sys.stdin = open("input.txt","r")

result = []
for t in range(1,int(input())+1):
    L,U,X = map(int,input().split())
    if X<L:
        ans = L-X
    elif X>U:
        ans = -1
    else:
        ans = 0
    result.append(f'#{t} {ans}')
print('\n'.join(result))
    