def divied(end,A,B):
    global answer
    if 1<= A <= end//2 and end//2+1 <= B <= end:
        answer = len(bin(end))-3
    if 1<= A <= end//2 and 1<= B <= end//2:
        divied(end//2,A,B)
    if end//2+1 <= A and end//2+1<=B:
        divied(end//2,A-end//2,B-end//2)


def solution(n,a,b):
    global answer
    divied(n, min(a, b), max(a, b))
    return answer

answer = 1
print(solution(8,4,7))
print(solution(8,1,3))