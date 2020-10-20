def solution(n):
    answer = 0
    dp = [0] *10001

    for i in range(1,10001):
        dp[i] = i * (i + 1) // 2
        tmp = 0
        while tmp<10000:
            if tmp * i > n:
                break
            if n == tmp*i + dp[i]:
                answer += 1
                break
            tmp += 1
    return answer
solution(15)