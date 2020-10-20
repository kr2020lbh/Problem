#10505. 소득 불균형
import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N = int(input())
    money = list(map(int,input().split()))
    AVG = sum(money)//N
    ans = 0
    for i in range(len(money)):
        if money[i] <= AVG:
            ans += 1
    print("#{} {}".format(t,ans))
