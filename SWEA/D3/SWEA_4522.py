for t in range(1,int(input())+1):
    word = input()
    if len(word)==1:
        print(f'#{t} Exist')
        continue
    result = 'Not exist'
    while len(word)>1:
        if word[0]=='?' or word[-1]=='?' or word[0]==word[-1]:
            word = word[1:-1]
            result = 'Exist'
        else: 
            result = 'Not exist'
            break
    print(f'#{t} {result}')