
def solution(citations):
    citations.sort()
    for h in range(0,citations[-1]+1):
        for i in range(len(citations)):
            if citations[i] < h and


citations = [1,1,2,2,2,2]
print(solution(citations))