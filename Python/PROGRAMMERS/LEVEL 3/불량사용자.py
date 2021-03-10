import re
from itertools import permutations
def solution(user_id, banned_id):
    ans = []
    cnt = 0
    banned_id = list(map(lambda x : ''.join(['[a-zA-Z0-9]{1,1}' if i =='*' else i for i in x]), banned_id))
    for perm in permutations(user_id,len(banned_id)):
        for i in range(len(perm)):
            if not re.fullmatch(banned_id[i],perm[i]):
                break
        else:
            for i in range(len(ans)):
                if set(ans[i]) == set(perm):
                    break
            else:
                ans.append(perm)
                cnt += 1
    return cnt


user_id1,banned_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]
user_id2,banned_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]
user_id3,banned_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]

solution(user_id1,banned_id1)
solution(user_id2,banned_id2)
solution(user_id3,banned_id3)