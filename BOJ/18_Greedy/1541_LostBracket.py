import sys
sys.stdin = open("input.txt","r")


r = input().split('-')
for i in range(len(r)):
    r[i] = r[i].split('+')
    tmp = 0
    for num in r[i]:
        tmp+=int(num)
    r[i] = tmp
print(int(r[0])-sum(r[1::]))