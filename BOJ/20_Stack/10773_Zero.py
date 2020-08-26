import sys
sys.stdin = open("input.txt","r")

N = int(input())
stack = [0] * N
top = 0
for i in range(N):
    num = int(input())
    if num != 0:
        stack[top]=num
        top += 1
    else:
        stack[top-1]=0
        top -= 1

print(sum(stack))