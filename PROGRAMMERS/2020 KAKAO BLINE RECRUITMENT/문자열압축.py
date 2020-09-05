import sys
sys.stdin=open("input.txt","r")
# def solution(s):
#     answer = 0
#     length = len(s)
#     tmp = list(s)
#     # 반복 단위의 최대인 length//2부터 시작한다.
#
#     for repeated_length in range(length // 2, 0, -1):
#         print(is_repeated(tmp, repeated_length),repeated_length)
#         if 1 in is_repeated(tmp, repeated_length):
#             pass
#
# def is_repeated(arr, n):
#     # 입력 문자열 arr에 대해서 반복 단위 n을 조사할 때
#     # 전체 길이에서 +1 - 2*n번 반복한다.
#     # ex 전체길이 10 반복단위 4일 때는 3번,
#     prev = arr[0:n]
#     cnt=[1]
#     i = n
#     while i<=len(arr)-n:
#         if prev == arr[i:i + n]:
#             cnt[-1]+=1
#             i += n
#         else:
#             cnt.append(1)
#             prev = arr[i:i+n]
#             i+=1
#     return cnt


#
# s = list(input())
# length = len(s)
# MIN = length
# for repeated_length in range(length // 2,0, -1):
#     i = 0
#     cnt = {}
#     prev=''
#     while i < length:
#         if prev == s[i:i+repeated_length]:
#             if cnt.get(''.join(prev), 0):
#                 cnt[''.join(prev)]+=1
#             else:cnt[''.join(prev)]=1
#         else:
#             prev = s[i:i+repeated_length]
#         i+=repeated_length
#
#     if len(cnt)!=0:
#
#         # print('#{} cnt={} length={}: '.format(t,cnt,repeated_length))
#         ttt = 0
#         for i in cnt.values():
#             ttt += (i+1)*repeated_length
#         # print(length-ttt+len(cnt)+repeated_length)
#         tmp =length-ttt+len(cnt)*repeated_length+len(cnt)
#         if MIN > tmp:
#             MIN = tmp
#
# print('MIN=',MIN)


def solution(s):
    length = len(s)
    MIN = length
    for i in range(length // 2+1):
        print(s[0:i])
    for repeated_length in range(length // 2, 0, -1):
        i = 0
        cnt = {}
        prev = ''
        while i < length:
            if prev == s[i:i + repeated_length]:
                if cnt.get(''.join(prev), 0):
                    cnt[''.join(prev)] += 1
                else:
                    cnt[''.join(prev)] = 1
            else:
                prev = s[i:i + repeated_length]
            i += repeated_length

        if len(cnt) != 0:
            SUM = 0
            SUM2 = 0
            for i in cnt.values():
                SUM += (i + 1) * repeated_length
                SUM2 += len(str(i))
            tmp = length-SUM+len(cnt)*repeated_length+SUM2
            if MIN > tmp:
                MIN = tmp
    return MIN
for t in range(1,5):
    print(t,solution(input()))