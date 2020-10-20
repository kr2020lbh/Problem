def solution(arr):
    start =max(arr)
    while True:
        for num in arr:
            if start % num != 0:
                break
        else:
            return start
        start+=1


print(solution([2,6,8,14]))