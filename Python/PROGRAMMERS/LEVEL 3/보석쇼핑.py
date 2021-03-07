def solution(gems):
    cnt = len(set(gems))
    answer = [0,len(gems)]
    start,end = 0,0
    gems_dict = {gems[0] : 1}
    while start < len(gems) and end < len(gems):
        if len(gems_dict) == cnt:
            if answer[1] - answer[0] > end - start:
                answer = [start+1,end+1]
            if gems_dict.get(gems[start]):
                gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
        else:
            end += 1

            if end == len(gems):
                break
            if gems_dict.get(gems[end]):
                gems_dict[gems[end]] += 1
            else:
                gems_dict[gems[end]] = 1

    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])