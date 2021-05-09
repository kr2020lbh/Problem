def check(n,k):
    fact = factorial(n-1)
    for i in range(1,n+1):
        if fact * i>= k:
            return i
    return i

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def solution(n, k):
    originArr = list(range(1,n+1))
    answer = []
    for i in range(n,0,-1):
        checkResult = check(i,k)
        k -= (checkResult-1) * factorial(i-1)
        answer.append(originArr[checkResult-1])
        originArr.pop(checkResult-1)
    return answer

solution(3,5)