#초심자의 회문 검사
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    words = input()
    ans = 1
    for i in range((len(words)+1)//2):
        if words[i] != words[-1-i]:
            ans = 0
            break
    print(f'#{t} {ans}')