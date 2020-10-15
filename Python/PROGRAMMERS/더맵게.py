import heapq
def solution(scoville, k):
    heap = []
    for food in scoville:
        heapq.heappush(heap,food)
    answer = 0
    while len(heap) > 0:
        if heap[0] < k:
            if len(heap) == 1:
                return -1
            answer+=1
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            heapq.heappush(heap,a+b*2)
        else:
            return answer
    return -1


scoville = [1,2]
k = 2
print(solution(scoville,k))