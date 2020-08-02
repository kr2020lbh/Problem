#정곤이의 단조 증가하는 수

#1. 단조증가인지 확인하는 함수를 만든다
#2. 주어진 N개의 수를 각 곱하여 (이중반복문으로) 그 수가 단조증가인지 확인
#3. 단조증가라면 그 전 단조증가 수와 비교하여 최대값 결정

def is_increase(number):
    str_number = str(number)
    
    tmp = str_number[0]
    for num in str_number:
        if num < tmp:
            return False
        else:
            tmp = num
    else:
        return True

T=int(input())

for t in range(1,T+1):
    MAX=-1
    flag = False
    N=int(input())
    numbers = list(map(int,input().split()))
    for i in range(N-1):
        for j in range(i+1,N):
            flag = is_increase(numbers[i]*numbers[j])
            if flag:
                if numbers[i]*numbers[j] > MAX:
                    MAX = numbers[i]*numbers[j]
    print(f'#{t} -1') if (flag==False and MAX==0) else print(f'#{t} {MAX}')