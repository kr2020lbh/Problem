import sys
sys.stdin = open("input.txt","r")



N = int(input())
stack = []
top = -1
num = 1
result = []

def dfs():
    global top
    global num
    stack.append(num)
    result.append('+')
    top+=1
    num+=1

for _ in range(N):
    if len(stack) == 0:
        dfs()
    target = int(input())
    if target < stack[top]:
        result = False
        break

    elif target > stack[top]:
        while target!=stack[top]:
            dfs()

    result.append('-')
    del stack[top]
    top -= 1

if result:
    [print(r) for r in result]
else:
    print('NO')


