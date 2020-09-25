import sys
sys.stdin = open("input.txt","r")
l_b = '(['
r_b = ')]'
def dfs():
    global top
    if len(stack)==0:
        return
    else:
        result = stack[top-1]
        del stack[top-1]
        top -= 1
        return result


while True:
    stack = []
    top = 0
    txt = input()
    while txt[-1]!='.':
        txt+=input()

    if len(txt) == 1 and txt == '.':
        break
    else:
        for char in txt:
            if char in l_b:
                stack.append(char)
                top += 1
            elif char == ')':
                if dfs() != '(':
                    print('no')
                    break
            elif char == ']':
                if dfs() != '[':
                    print('no')
                    break
        else:
            if len(stack) != 0:
                print('no')
            else:
                print('yes')


