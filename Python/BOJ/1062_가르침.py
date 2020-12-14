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
base_alpha = {'a','n','t','i','c'}
from_word_alpha = set()
for _ in range(N):
    word = input()
    words.append(word)
    word = word[4:len(word)-4]
    for w in word:
        from_word_alpha.add(w)
to_select_word = from_word_alpha-base_alpha
base_alpha = list(base_alpha)

ans = 0
if K-len(base_alpha) >= 0:
    if len(to_select_word) > K-len(base_alpha):
        for k_alpha in combinations(to_select_word,K-len(base_alpha)):
            k_alpha = base_alpha + list(k_alpha)
            cnt = 0
            for word in words:
                if check(word,k_alpha):
                    cnt += 1
            if ans < cnt:
                ans = cnt
    else:
        ans = N
print(ans)
