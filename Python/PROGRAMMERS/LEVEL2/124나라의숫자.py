def solution(tmp):

    answer = ''
    i = 1
    total = 0


    while True:
        total += 3**i
        if tmp <= total:
            break
        i+=1
    # 3**(i-1)부터 시작했을 때 x 번째 수
    # tmp - 3**(i-1) = x 번 째 수
    # answer는 i 자리 수
    # answer의 i 번 쨰 수를 정하는 방법은
    #  x가 2*3**(i-1) 보다 크면 4
    #  x가 3**(i-1) 보다 크면 2
    #  x가 3**(i-1) 같거나 작으면 1


    #

    for j in range(i-1,-1,-1):
        tmp -= 3 ** (j - 1)

        if tmp > 2*3**(j):
            answer += '4'
            tmp -= 2*3**(j)
            continue

        if tmp > 3**(j):
            answer += '2'
            tmp -= 3**(j)
            continue

        answer += '1'

    return answer




for i in range(1,100):
    solution(i)
for i in range(100):
    print(3**i>4**(i-1))