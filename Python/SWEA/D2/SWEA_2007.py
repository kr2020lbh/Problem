#패턴 마디의 길이
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    words = input()
    for pattern in range(1,11):
        if words[:pattern]==words[pattern:pattern*2]:
            print(f'#{t} {pattern}')
            break
