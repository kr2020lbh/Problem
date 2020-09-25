#최장 공통 부분 수열
#예를 들어 "acaykp"와 "capcak"의 경우, 두 문자열의 최대 공통 부분 수열은 "acak"로 길이가 4이다.
import sys
import pprint
sys.stdin = open("input.txt","r")


for t in range(1,int(input())+1):
    first, second = input().split()
    max_lcs = 0
    row = len(first)+1
    col = len(second)+1
    lcs = [[ 0 for j in range(col) ] for i in range(row)]

    for i in range(1, row):
        for j in range(1,col):
            if first[i-1]!=second[j-1]:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
            else:
                lcs[i][j] = lcs[i-1][j-1]+1
        if max_lcs < lcs[i][j]:
            max_lcs =lcs[i][j]
    print(f'#{t} {max_lcs}')
