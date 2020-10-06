import sys
sys.stdin = open("input.txt","r")

N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
#postorder의 가장 오른쪽 node1은 루트 노드
#inorder에서 node1을 기준으로 왼쪽 분기 branch1 오른쪽 분기 branch2를 나눈다.
#postorder에서 branch1의 가장 오른쪽 node2는 루트 노드, branch2의 가장 오른쪽 node3는 루트 노드
#이렇게 반복적으로 수행하면 트리의 형태를 파악할 수 있다

preorder = []
for i in range(N):
    if inorder[i]==postorder[i]:
        continue
    else:
        idx = i
        break
preorder+=inorder[0:idx+1][::-1]
tmp = postorder[idx:N-1]
a = []
b = []
for i in range(len(tmp)):
    if i%2==0:
        a.append(tmp[i])
    else:
        b.append(tmp[i])
preorder+=a[::-1]+b

print(*preorder)

