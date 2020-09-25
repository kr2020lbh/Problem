# 1부터 N까지 담은  str 리스트 생성
# 그 중 K개 제거
for t in range(int(input())):
    N,K = map(int,input().split())
    myList = [str(i) for i in range(1,N+1)]
    delList = list(map(str,input().split()))
    for delete in delList:
        myList.remove(delete)
    print(f"#{t+1} {' '.join(myList)}")