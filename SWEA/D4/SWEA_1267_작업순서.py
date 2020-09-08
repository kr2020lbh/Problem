import sys
sys.stdin = open("input.txt","r")


# 처음에는 bfs를 V번 실행하면 저절로 모든 노드를 방문할줄 알았다 이 때문에 다른것에 오류가 있는지
# 한참 고민하다가.. 선행 방문 조건에 의해서 V번 실행해도 방문하지 못하는 노드가 있다는 것을 알고,
# print하는 횟수로 V번 실행 되었는지 확인하도록 while 조건문에 추가했더니 PASS..

def bfs():
    global cnt

    for i in range(1,V+1):
        # i 노드를 방문하지 않았다면, 선행 방문 조건이 필요하진 조사해본다.
        if visited[i]==0:
            for v in edges[i]:
                # i 노드에 있는 숫자들은 선행 방문 해야할 노드들이다.
                # 만약 0이라면 선행 방문하지 않았으므로 break 후 다음 노드 조사해본다.
                if visited[v] == 0:
                    break
            #위의 조건문을 지났다는 것은 선행방문이 완료되었다는 것
            #따라서 출력 후, cnt += 1
            else:
                visited[i] = 1
                print(i, end=' ')
                cnt+=1


for t in range(1,11):
    V,E = map(int,input().split())
    tmp = list(map(int, input().split()))

    edges = [[] for _ in range(V+1)]
    Q = []
    visited = [0]*(V+1)

    #w 노드에 v를 추가한다.
    #w 노드를 방문하려면 v 노드를 선행 방문해야한다.

    for i in range(E):
        v,w = tmp[i*2],tmp[i*2+1]
        edges[w].append(v)

    print("#{}".format(t),end=' ')
    cnt=0
    while True:
        if cnt == V:
            break
        bfs()
    print()
