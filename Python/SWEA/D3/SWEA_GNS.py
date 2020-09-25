import sys
sys.stdin = open("input.txt","r")

GNS=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1,int(input())+1):
    tc = input().split()
    words = input().split()
    #입력에 들어있는 GNS 요소 단어들의 수를 나타내는 배열
    number=[0]*10
    for word in words:
        for idx,element in enumerate(GNS):
            if element == word:
                #입력에 있는 단어가 어떤 단어인지 확인 후
                #그 단어 수를 하나 증가
                number[idx]+=1
                break

    print(tc[0])
    for i in range(10):
        print((GNS[i]+' ')*number[i],end=' ')
    print()


GNS=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1,int(input())+1):
    tc = input().split()
    number=[0]*10
    for word in input().split():
        number[GNS.index(word)]+=1

    print(tc[0])
    [print((GNS[i]+' ')*number[i],end=' ') for i in range(10)]
    print()


