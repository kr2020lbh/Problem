def solution(routes):
    routes.sort(key=lambda x:(x[1],x[0]))
    print(routes)
    prev = routes[0][1]
    answer = 0

    for i in range(1,len(routes)):
        now = routes[i][0]
        if now >= prev:
            answer += 1
        prev = now
    print(answer)
    return answer



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)