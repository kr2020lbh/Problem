
def solution(a):
    left_value = [0] * len(a)
    right_value = [0] * len(a)
    left_min = a[0]
    right_min = a[-1]
    left_value[0] = left_min
    answer = 2
    for i in range(len(a)):
        if a[i] < left_min:
            left_min = a[i]
        left_value[i] = left_min

    for i in range(len(a)-1,-1,-1):
        if a[i] < right_min:
            right_min = a[i]
        right_value[i] = right_min

    for i in range(1,len(a)-1):
        if a[i] <= left_value[i] or a[i] <= right_value[i]:
            answer += 1
    return answer
solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]	)
solution([1,2,3])