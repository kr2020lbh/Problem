for t in range(1,int(input())+1):
    word = list(input())
    H = int(input())
    locations = sorted(list(map(int, input().split())))
    i=0
    for location in locations:
        location+=i
        word.insert(location,'-')
        i+=1
    result = ''.join(word)
    print(f'#{t} {result}')