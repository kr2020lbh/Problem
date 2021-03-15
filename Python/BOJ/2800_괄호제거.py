import sys
sys.stdin = open("input.txt","r")

from itertools import combinations
brackets = list(input())
stack,indexes,ans = [],[],set()
for idx,val in enumerate(brackets):
    if val == '(':
        stack.append(idx)
        brackets[idx] = ''
    if val == ')':
        brackets[idx] = ''
        indexes.append([stack.pop(),idx])

for i in range(len(indexes)):
    for comb in combinations(indexes,i):
        tmp = brackets[::]
        for front,rear in comb:
            tmp[front] = '('
            tmp[rear] = ')'
        ans.add(''.join(tmp))

[print(a) for a in sorted(ans)]