def solution(jobs):
    jobs.sort(key=lambda x:(x[1],x[0]))
    visited = [False] * len(jobs)
    start = cnt = answer = 0
    while cnt != len(jobs):
        closest = 1001
        for i in range(len(jobs)):
            if visited[i] == False:
                if jobs[i][0] <= start:
                    visited[i] = True
                    answer += start - jobs[i][0] + jobs[i][1]
                    start += jobs[i][1]
                    break
                else:
                    if jobs[i][0] < closest:
                        closest = jobs[i][0]
                        idx = i
        else:
            visited[idx] = True
            answer += jobs[idx][1]
            start = jobs[idx][0] + jobs[idx][1]
        cnt+=1
    return answer // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)
solution([[0,4],[0,3],[0,2],[0,1]])
solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]])
solution([[0, 3], [1, 9], [500, 6]])
solution([[0,1],[100,1],[200,1]])