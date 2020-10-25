from collections import deque
def solution(cacheSize, cities):
    Q = deque(maxlen=cacheSize)
    answer = 0

    for city in cities:
        city = city.lower()

        if city in Q:
            Q.remove(city)
            Q.append(city)
            answer += 1

        else:
            Q.append(city)
            answer += 5

    return answer


# solution(3,	['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])
# solution(3,['Jeju', 'Pangyo', 'Seoul','LA', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'])
solution(0,['Jeju', 'Pangyo', 'Seoul','LA'])