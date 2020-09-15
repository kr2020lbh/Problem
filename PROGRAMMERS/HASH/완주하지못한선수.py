def solution(participant, completion):
    p_dict = {}
    for p in participant:
        if p_dict.get(p):
            p_dict[p] += 1
        else:
            p_dict[p] = 1
    for c in completion:
        if p_dict.get(c):
            p_dict[c]-=1
    print()
    return sorted(list(p_dict.items()),key=lambda x:x[1])[-1][0]