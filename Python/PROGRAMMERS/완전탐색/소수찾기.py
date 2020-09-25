def f(numbers, length, cur_num, visited,res):
    if len(cur_num) == length:
        res.add(int(cur_num))
    else:
        for i in range(len(numbers)):
            if i not in visited:
                visited.append(i)
                f(numbers, length, cur_num+numbers[i], visited,res)
                visited.pop()
    return res


def is_primary(num):
    if num==1 or num==0:return False
    cnt = 0
    for i in range(1,num+1):
        if num%i == 0:cnt+=1
        if cnt>2:return False
    return True



def solution(numbers):
    answer = 0
    res = set()
    for length in range(1, len(numbers)+1):
        res.update(f(numbers,length,'',[],set()))
    for num in res:
        if is_primary(int(num)):
            answer+=1
    return answer

print(solution('011'))