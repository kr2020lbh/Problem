import sys
sys.stdin = open("input.txt","r")


def in_order(alphabet):
    #왼쪽 루트 오른쪽
    if alphabet == 0:
        return
    else:
        in_order(tree[ord(alphabet)-64][0])
        print(alphabet,end='')
        in_order(tree[ord(alphabet)-64][1])


def pre_order(alphabet):
    #루트 왼쪽 오른쪽
    if alphabet == 0:
        return
    else:
        print(alphabet, end='')
        pre_order(tree[ord(alphabet)-64][0])
        pre_order(tree[ord(alphabet)-64][1])


def post_order(alphabet):
    #왼쪽 오른쪽 루트
    if alphabet == 0:
        return
    else:
        post_order(tree[ord(alphabet) - 64][0])
        post_order(tree[ord(alphabet) - 64][1])
        print(alphabet, end='')


N = int(input())
tree = [[0,0] for _ in range(N+1)]
for _ in range(N):
    parent,left_child,right_child = input().split()
    int_parent = ord(parent)-64
    if left_child != '.':
        int_left_child = ord(left_child) - 64
        tree[int_parent][0]=left_child

    if right_child != '.':
        int_right_child = ord(right_child) - 64
        tree[int_parent][1]=right_child

pre_order('A')
print()
in_order('A')
print()
post_order('A')