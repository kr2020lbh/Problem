def solution(n, s):
    if (s // n) == 0:return [-1]
    answer = []
    while n != 0:
        prev = s // n
        s = s - prev
        n = n -1
        answer.append(prev)
    return answer

solution(2,9)
solution(2,1)
solution(2,8)