#세가지 합 구하기
# N 들어오면 1~N, 홀수 N개 짝수 N개
import sys
sys.stdin = open("input.txt","r")
result =[]
for t in range(1,int(input())+1):
    N = int(input())
    a = N*(N+1)//2
    b = N**2
    c = 2*a
    result.append(f'#{t} {a} {b} {c}')
print('\n'.join(result))