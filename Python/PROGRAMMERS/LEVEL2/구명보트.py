def solution(people, limit):
    people.sort(reverse=True)
    first = 0
    last = len(people)-1
    answer = 0
    while first<last:
        if people[first] + people[last] > limit:
            first+=1
        else:
            first+=1
            last-=1
        answer+=1

    if first == last:
        answer += 1
    return answer


people =[40,40,40,40,40,40,60,60, 70]
limit = 100
solution(people,limit)