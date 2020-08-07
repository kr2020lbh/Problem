#조교의 성적 매기기
import sys
sys.stdin = open("input.txt","r")

def get_total_score(scores): #입력받은 점수를 비율에 따라 총점 만들기
    rates = [0.35, 0.45, 0.2]
    score = 0
    for j in range(3):
        score += scores[j] * rates[j]
    return  score


final_score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t in range(1,int(input())+1):

    N,K = map(int,input().split()) #학생의 수, 출력하고 싶은 학생의 번호
    arr = [] #N 명의 학생들 점수를 총점으로 변환한 점수를 담고 있는 배열

    for i in range(N):
        score = get_total_score(list(map(int, input().split())))
        arr.append([score,i])
        # 나중에 K 번째 학생의 점수를 찾기 위해 i를 같이 append한다,
        # enumerate 함수를 써도 된다!

    arr.sort(key=lambda x: x[0],reverse=True)
    # 학생들의 총점을 내림차순으로 정렬한다.
    # 이때 arr 배열에는 [[74.6,0],[92.5,1],[88.8,2]...] 이렇게 자료가 있는데
    # 총점을 기준으로 정렬하고 싶기 때문에 sort함수의 key argument를 활용해 기준을 정한다
    # 그 기준은 각각의 요소들 [74.6,0] [92.5,1]...[score,i] 에서 첫 번째 요소인 score가 기준이다
    # key = lambda x : x[0] 를 통해서 score를 기준으로 정렬하도록 만든다.
    # 또한 내림차순으로 정렬하기 때문에 reverse = True
    for i in range(N):
        if arr[i][1] == K-1:
        # 총점을 기준으로 내림차순으로정렬된 arr 안에서 K 번째 학생을 찾는다.
            print(f'#{t} {final_score[ i // (N//10)]}')
            # 그 K 번째 학생의 성적을 입력하기 위해서는
            # 10명의 학생이 있다면 각각 성적 A+, A0, A- ... 은 1명
            # 20명의 학생이 있다면 각각 성적 2명
            # N명의 학생이라면 N//2 명씩이다

            # 내림차순으로 정렬되어 있기 때문에 i 는 등수를 의미한다.
            # 10명 중 i 등이면 [A+, A0, A- ..] 의 i 번째 성적을 받는다.
            # 20명 중 i 등이면 [A+, A0, A- ..] 의 i//2 번째 성적을 받는다. (1등도 A+ 2등도 A+)
            #  N명 중 i 등이면 [A+, A0, A- ..] 의 i//(N//10)  번째 성적을 받는다.

