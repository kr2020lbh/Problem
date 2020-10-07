import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("input.txt","r")


def get_postOrder(start,end):
    if start>end:return
    root = preOrder[start]
    right_start = start
    for i in range(start,end+1):
        if root < preOrder[i]:
            right_start = i
            break

    if right_start == start:
        get_postOrder(start+1,end)
        print(root)
    else:
        get_postOrder(start + 1, right_start - 1)
        get_postOrder(right_start, end)
        print(root)



preOrder = []
while True:
    try:
        preOrder.append(int(input()))
    except:
        break

pos = [0]*10**6
for i in range(len(preOrder)):
    pos[preOrder[i]] = i
get_postOrder(0,len(preOrder)-1)