answer = 1000

def dfs(words,cur_word,target,depth,visited):
    global answer
    if depth > answer:
        return
    if target == cur_word:
        answer = depth
    for i in range(len(words)):
        if not(visited & (1<<i)):

            if differ(words[i],cur_word):
                dfs(words,words[i],target,depth+1,visited|(1<<i))


def differ(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
            if cnt > 2:
                return False
    if cnt == 1:
        return True

def solution(begin, target, words):
    if target in words:
        dfs(words,begin,target,0,0)
        return answer
    else:
        return 0
words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin = "hit"
target = "cog"
print(solution(begin,target,words))