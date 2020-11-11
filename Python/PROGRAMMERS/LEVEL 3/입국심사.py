#가장 오래걸리는 시간부터 이분탐색.........
#원하는 값을 찾았어도 더 최소 값을 가질 수 있기 떄문에 left <= right 조건을 가지고 계속 이분탐색....
def solution(n, times):
    answer,left,right = 0,1,max(times)*n

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in times:
            total += mid // i
            if total >= n:
                answer = mid
                right = mid - 1
                break
        else:
            left = mid + 1

    return answer

solution(6,[7,10])
solution(18,[7,8,10,11,100])