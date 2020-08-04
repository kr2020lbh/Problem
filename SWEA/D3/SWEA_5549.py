#홀수일까 짝수일까
# #숫자를 str로 입력받아 확인하기
for t in range(int(input())):
    print(f'#{t+1} Odd') if int(input()[-1])%2 else print(f'#{t+1} Even')