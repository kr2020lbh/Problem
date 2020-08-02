# 그리고 해당 인덱스에 있는 문자를 반환하는 함수를 만든다
# 1~5번째 배열의 
# 첫번째 요소를 다 더하고, 
# 두번째 요소를 다 더하고, ...
# 열다섯번째 요소까지 다 더 한다
def get_char_by_idx(idx, mylist):
    if idx>=len(mylist):
        return ''
    else:
        return mylist[idx]
    
for t in range(int(input())):
    tmpList = []
    for i in range(5):
        result = ''
        word = list(map(str,input()))
        tmpList.append(word)
    for idx in range(15):
        for j in range(5):
            result +=get_char_by_idx(idx,tmpList[j])
    print(f'#{t+1} {result}')