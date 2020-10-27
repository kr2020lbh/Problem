num_to_alpha = ['A','B','C','D','E','F']
def n_by_number(n,t,m,p):
    res = '0'
    for number in range(t*m+1):
        tmp = ''
        while number != 0:
            q = number // n
            r = number % n
            number = q
            if r > 9 :
                tmp += num_to_alpha[r-10]
            else:
                tmp += str(r)
        res+=tmp[::-1]
    answer=''
    for i in range(0,len(res),m):
        answer += res[i:i+m][p-1]
        if len(answer) == t:
            return answer


def solution(n, t, m, p):
    return n_by_number(n,t,m,p)

print(solution(16,16,2,1))
