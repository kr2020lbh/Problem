def solution(s):
    positive = []
    negative = []

    for i in s.split():
        if i[0] != '-':
            positive.append(int(i))
        else:
            negative.append(int(i[1::]))

    positive.sort()
    negative.sort()

    if positive and negative:
        MAX = positive[-1]
        MIN = -negative[-1]
    elif positive:
        MAX = positive[-1]
        MIN = positive[0]
    else:
        MAX = -negative[0]
        MIN = -negative[-1]

    answer = str(MIN) + ' ' + str(MAX)
    return answer

solution("13 2 -3 4")