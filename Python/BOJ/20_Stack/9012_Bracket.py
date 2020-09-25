import sys
sys.stdin = open("input.txt","r")
def check():
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack)==0:
                return 'NO'
            else:
                stack.pop()
    else:
        if stack:
            return 'NO'
        else: return 'YES'
N = int(input())
for i in range(N):
    brackets = input()
    print(check())