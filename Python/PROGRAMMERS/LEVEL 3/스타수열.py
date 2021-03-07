from collections import Counter
def solution(a):
    cnt = Counter(a)
    answer = -1 
    for key in cnt.keys():
        if cnt[key] <= answer:
            continue
        else:
            tmp_answer = 0
            idx = 0
            while idx < len(a)-1:
                if (a[idx] == a[idx+1]) or (a[idx]!=key and a[idx+1]!=key):
                    idx += 1
                else:
                    tmp_answer += 1
                    idx += 2
            answer = max(tmp_answer,answer)
    print(answer)
solution([0])
solution([5,2,3,3,5,3])
solution([0,3,3,0,7,2,0,2,2,0])
