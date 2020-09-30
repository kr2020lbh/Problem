import sys
sys.stdin = open("input.txt","r")
#지역의 수가 N 일 때
#1~N//2 만큼 지역을 나눈다, 왜냐면 1,N-1와 N-1,1 은 같기 때문이다
#target 이 1부터 N//2 일 때
#지역을 나누기 위해서 1~N의 지역을 target 개수 만큼 뽑는 조합을 이용했다.
#조합으로 뽑은 수와 나머지 수를 left, right로 나눠 각자 connected 되어 있는지 확인한다.
#둘 다 connected 되어 있다면, 인구 수를 구하고 둘의 차를 MIN과 비교하여 더 작다면 MIN으로 할당한다.

#나는 처음에 target 수 만큼 이어져 있는 지역을 구하려 애썼다. 하지만 그 과정에서 시간초과가 나왔다.
#왜냐하면 조합이 아닌 방법으로 구했기 떄문에 [1,2,6],[2,1,6],[6,1,2]와 같이 중복으로 지역을 나눴고 이 때문에
#connected 확인하는 작업을 이미 한 지역에 대해서도 했기 떄문이다.
#내장함수 combination이 아닌 방법으로 풀려고 노력했는데 잘 되지 않았다.
from itertools import combinations
from collections import deque


def select(target):
    return(list(combinations(nums,target)))


def get_seperated(arr):
    tmp = set(range(N))
    seperated = tmp-set(arr)
    return list(seperated)


def is_connected(selected):
    selected = list(selected)
    Q = deque()
    Q.append(selected[0])
    visited = [selected[0]]
    while Q:
        cur = Q.popleft()
        for idx,a in enumerate(arr[cur]):
            if a == 1 and idx in selected and idx not in visited:
                visited.append(idx)
                Q.append(idx)
        if set(visited) == set(selected):
            return True
    return False


N = int(input())
population = list(map(int,input().split()))
arr = [[0]*(N) for _ in range(N)]
nums = range(N)
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(1,tmp[0]+1):
        arr[i][tmp[j]-1] = 1
MIN =10000
for target in range(1,N//2+1):
    for a in select(target):

        left = list(a)
        right = get_seperated(left)
        if is_connected(left) and is_connected(right):
            left_sum = right_sum = 0
            for i in range(len(left)):
                left_sum+=population[left[i]]
            for i in range(len(right)):
                right_sum+=population[right[i]]
            if MIN > abs(left_sum-right_sum):
                MIN = abs(left_sum-right_sum)

if MIN == 10000:
    print(-1)
else:
    print(MIN)