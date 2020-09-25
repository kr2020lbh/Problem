import sys
sys.stdin = open("input.txt","r")

def find_common_parent(arr1,arr2):
    for element1 in arr1:
        for element2 in arr2:
            if element1==element2:
                return element1


def count_subtree(root):
    Q = [*nodes1[root]]
    count = 1
    while Q:
        v=Q.pop()
        count+=1
        Q.extend(nodes1[v])
    return count


def parent_list(i):
    parent = []
    while True:
        if not nodes2[i]:break
        parent.extend(nodes2[i])
        i=nodes2[i][0]
    return parent


for t in range(1,int(input())+1):
    V,E,node1,node2 = map(int,input().split())
    edges = list(map(int,input().split()))
    nodes1 = [[] for i in range(V + 1)]
    nodes2 = [[] for i in range(V + 1)]
    for i in range(E):
        nodes1[edges[i * 2]].append(edges[i * 2 + 1])
        nodes2[edges[i * 2 + 1]].append(edges[i * 2])

    ans1=find_common_parent(parent_list(node1),parent_list(node2))
    ans2=count_subtree(ans1)
    print("#{} {} {}".format(t,ans1,ans2))