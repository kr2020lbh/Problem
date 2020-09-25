#Digit sum
import sys
sys.stdin = open("input.txt","r")

# def f(N):
#     return int(N) if len(N)==1 else f(str(sum([ int(n) for n in N ])))

# ans=[]
# T = int(input())
# for t in range(1,T+1):
#     ans.append(f'#{t} {f(input())}')
# for t in range(T):
#     print(ans[t])

T = int(input())
ans=[]
for t in range(1,T+1):
    
    N = input()
    while(len(N)>1):
        N = str(sum([int(n) for n in N]))
    ans.append(f'#{t} {N}')
for t in range(T):
    print(ans[t])

