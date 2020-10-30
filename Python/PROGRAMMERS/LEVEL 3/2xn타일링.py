def solution(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    for i in range(n-2):
        b,a = a+b,b
    return b % 1000000007
print(solution(60000))