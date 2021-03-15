import sys
sys.stdin = open("input.txt","r")
N,K = map(int,input().split())
Q = [i for i in range(1,N+1)]
k = 0
ans = []
for i in range(N):
    k = (k+K-1) % len(Q)
    ans.append(str(Q.pop(k)))
    

print('<{}>'.format(', '.join(ans)))
        