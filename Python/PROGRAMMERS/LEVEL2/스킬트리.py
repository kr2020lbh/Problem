def check(skill_tree,user_skill):
    for s in user_skill:
        if s in skill_tree:
            if s != skill_tree[0]:
                return False
            else:
                skill_tree.pop(0)
    return True

def solution(skill,skill_trees ):
    answer = 0
    for user_skill in skill_trees:
        tmp = list(skill)[::]
        if check(tmp,user_skill):
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill,skill_trees)