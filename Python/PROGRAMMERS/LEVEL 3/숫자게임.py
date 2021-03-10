def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(B)):
        if A[i] < B[i]:
            answer += 1
        else:
            for j in range(i+1,len(B)):
                if A[i] < B[j]:
                    B[i],B[j] = B[j],B[i]
                    answer += 1
                    break
    return answer
A,B =[5,1,3,7],[2,2,6,8]
a,b = [2,2,2,2],[1,1,1,1]
solution(A,B)


def solution(A, B):
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            j += 1

    return j