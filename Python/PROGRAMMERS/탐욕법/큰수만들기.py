def solution(number, k):
    to_select = len(number)-k
    answer = ''
    start = 0

    while to_select!=0:

        if len(number) - start == to_select-1:
            answer += number[start::]
            break

        MAX = 0

        for idx in range(start, len(number) - to_select + 1):
            if int(number[idx]) > MAX:
                start = idx
                MAX = int(number[idx])
                if MAX == 9:break

        answer += number[start]
        start+=1
        to_select -= 1

    return answer

number = '4177252841'
k = 4
solution('1924',2)