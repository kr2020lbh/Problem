#간단한 369게임

for number in range(1,int(input())+1):
    count = 0
    for n  in str(number):
        if n in '369':
            count+=1
    if count:ans = '-'*count
    else:ans = number
    print(f'{ans}',end = ' ')
