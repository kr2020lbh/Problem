import sys
sys.setrecursionlimit(10**6)
class Tree:
    def __init__(self,data,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def print_node(self):
        cur = self.data
        left = self.left
        right = self.right
        print('cur_node_data',cur)
        while left:
            if left:
                print('left',left.data)
                left.print_node()
                left = left.left
            else:
                break
        while right:
            print('right',right.data)
            if right:
                right.print_node()
                right = right.right
            else:
                break

        print('parent',self.parent.data if self.parent else None)
        
            

def solution(nodeinfo):
    tree = [[] for _ in range(1001)]
    for i in range(len(nodeinfo)):
        x,y = nodeinfo[i]
        if tree[y]:
            for j in range(len(tree[y])):
                if tree[y][j][0] < x:
                    continue
                else:
                    tree[y].insert(j-1,[x,y,i+1])
        else:
            tree[y].append([x,y,i+1])
    
    for i in range(len(tree)-1,-1,-1):
        if tree[i]:
            node = Tree(tree[i][0])
            break
    find_right(node,tree)
    node.print_node()

def find_right(node,tree):
    x,y,idx = node.data
    parent = node.parent
    if parent:
        while True:
            parent = node.parent.parent
            if not parent:
                break        
    else:
        parent = None

    flag = False

    for i in range(y-1,-1,-1):
        for j in range(len(tree[i])):
            nx,ny,nidx = tree[i][j]
            if parent:
                if parent.data < nx and x < nx:
                    node.right = Tree(tree[i][j],None,None,node)
                    flag = True
                    find_right(node.right,tree)
                    return
            else:
                if x < nx:
                    node.right = Tree(tree[i][j],None,None,node)
                    flag = True
                    find_right(node.right,tree)
                    return

            
solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)
