import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10)

#postorder의 가장 오른쪽 node1은 루트 노드
#inorder에서 node1을 기준으로 왼쪽 분기 branch1 오른쪽 분기 branch2를 나눈다.
#postorder에서 branch1의 가장 오른쪽 node2는 루트 노드, branch2의 가장 오른쪽 node3는 루트 노드
#이렇게 반복적으로 수행하면 트리의 형태를 파악할 수 있다

def get_preorder(inorder_start,inorder_end,postorder_start,postorder_end):
    if postorder_end<postorder_start or inorder_end < inorder_start:return
    inorder_center_index = pos[POSTORDER[postorder_end]]
    ans.append(INORDER[inorder_center_index])
    get_preorder(inorder_start,inorder_center_index-1,postorder_start,postorder_start+inorder_center_index-1-inorder_start)
    get_preorder(inorder_center_index+1,inorder_end,postorder_start+inorder_center_index-inorder_start,postorder_end-1)


N = int(input())
pos = [0] * (N+1)

INORDER = list(map(int,input().split()))
POSTORDER = list(map(int,input().split()))
for i in range(N):
    pos[INORDER[i]] = i

ans = []
get_preorder(0,N-1,0,N-1)
print(*ans)