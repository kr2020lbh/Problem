import heapq
def solution(n, works):
    h = []
    length = len(works)
    for i in range(length):
        heapq.heappush(h,-works[i])
    for i in range(n):
        heapq.heappush(h,heapq.heappop(h)+1)
    answer = 0
    for i in range(length):
        if h[i] < 0:
            answer += h[i]**2
    return answer

solution(4,[4,3,3])
solution(3,[1,1])
solution(1,[2,1,2])



