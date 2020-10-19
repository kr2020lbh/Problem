def decimal_to_binary(n):
    binary = []
    while n>1:
        mod = n%2
        n = n//2
        binary.append(mod)
    binary.append(n)
    return binary[::-1]


def count_one(binary):
    one = 0
    for i in binary:
        if i == 1:
            one += 1
    return one

def solution(n):
    answer = n+1
    n = count_one(decimal_to_binary(n))
    while True:
        if n == count_one(decimal_to_binary(answer)):
            return answer
        answer+=1
    return answer
solution(9)