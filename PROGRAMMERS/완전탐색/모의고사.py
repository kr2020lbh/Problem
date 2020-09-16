def f(index,method):
    return method[index%len(method)]

def solution(answers):
    methods = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    res = [[i+1,0] for i in range(3)]
    for idx,answer in enumerate(answers):
        for i in range(3):
            if f(idx,methods[i])==answer:
                res[i][1]+=1
    res.sort(key=lambda x:(-x[-1],x[0]))
    MAX  = res[0][1]
    answer = [res[0][0]]
    for i in range(1,3):
        if MAX == res[i][1]:
            answer.append(res[i][0])
    return answer

answers= [1,2,3,4,5]
solution(answers)
'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
'''