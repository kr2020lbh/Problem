def solution(n, results):
    people = []
    for i in range(n+1):
        people.append([set(),set()])

    for result in results:
        x,y = result
        people[x][0].add(y)
        people[y][1].add(x)

    for i in range(1,n+1):
        win,lose = people[i]
        for w in win:
            for l in lose:
                people[w][1].add(l)
                people[l][0].add(w)
    answer = 0
    for i in range(1,n+1):
        if len(people[i][0]) + len(people[i][1]) == n-1:
            answer += 1
    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])