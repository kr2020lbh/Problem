# 1월 1일은 금요일  4
# 각 월별 날짜 수와 주어진 날짜 수를 더해 7로 나누는 과정
days = [31,29,31,30,31,30,31,31,30,31,30,31]
for t in range(int(input())):
    result = 4
    m,d = map(int,input().split())
    print(f'#{t+1} {(sum(days[0:m-1])+d - 1 + result )%7}')