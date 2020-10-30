def solution(n):
    num_range = [1] * 20
    for i in range(1, 20):
        num_range[i] = num_range[i - 1] + 3 ** i
        if n < num_range[i]:
            idx = i
            break
    # print(idx) # idx 자리수
    cnt = n-num_range[idx-1]+1 #idx자리수 이면서 cnt 번째
    # print(n-num_range[idx-1]+1)
    res = ''
    for i in range(idx-1,-1,-1):#idx자리부터 1자리까지 구하기
        if cnt <= 3**i:
            res += '1'
        elif cnt <= 2*3**i:
            res += '2'
            cnt -= 3**i
        else:
            res += '4'
            cnt -= 2*3**i
    return res



