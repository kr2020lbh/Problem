#새샘이의 7-3-5 게임

# 무식하게 접근해보자
# 7개의 숫자를 3개를 뽑아 합을 새로운 리스트에 추가한다
# 이 리스트에서 중복 수를 없애고, 다시 정렬시켜 5번째로 큰 수를 출력한다
T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    sum_list = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            for k in range(j+1,len(numbers)):
                sum_list.append(numbers[i]+numbers[j]+numbers[k])
    result = sorted(list(set(sum_list)))
    print(f'#{t} {result[-5]}')