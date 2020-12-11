import sys
sys.stdin = open("input.txt","r")
from itertools import combinations

def check(word,k_alpha):
    for i in range(len(word)):
        if word[i] not in k_alpha:
            return False
    return True


N,K = map(int,input().split())
words = []
alpha = set()
for _ in range(N):
    word = input()
    word = word[4:len(word)-4]
    words.append(sorted(word))
words.sort(key=lambda x:(x,len(x)))
print(words)
alpha = list(alpha)
if len(alpha) > K:
    ans = 0
    for k_alpha in combinations(alpha,K):
        cnt = 0
        for word in words:
            if check(word,k_alpha):
                cnt += 1
        if ans < cnt:
            ans = cnt
else:
    ans = N
print(ans)

