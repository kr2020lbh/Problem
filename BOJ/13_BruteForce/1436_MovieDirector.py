import sys
sys.stdin = open("input.txt","r")
result= []
n=1
while len(result)<10000:
    if '666' in str(n):
        result.append(n)
    n+=1
N = int(input())
print(result[N-1])