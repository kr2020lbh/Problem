words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?","?????"]



#각 분기점에 대해서 단어가 추가될 때 cnt+=1
class Node:
    def __init__(self):
        self.child = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self,word):
        tmp = self.head
        for char in word:
            if char not in tmp.child:
                tmp.child[char] = Node()
            tmp = tmp.child[char]
            tmp.count+=1


    def search(self,word):
        cnt = 0
        if word == '':
            for value in self.head.child.values():
                cnt+=value.count
            return cnt

        tmp = self.head
        for char in word:
            if tmp.child.get(char):
                tmp = tmp.child[char]
                cnt = tmp.count
            else:
                return 0
        return cnt

def solution(words, queries):
    foward_words = [Trie() for i in range(10001)]
    reverse_words = [Trie() for i in range(10001)]

    for word in words:
        foward_words[len(word)].insert(word)
        reverse_words[len(word)].insert(word[::-1])

    answer = [0 for _ in range(len(queries))]
    for index,query in enumerate(queries):
        if query[0] != '?':
            q =query.split('?')[0]
            answer[index] = foward_words[len(query)].search(q)
        else:
            q = query.split('?')[-1]
            answer[index] = reverse_words[len(query)].search(q[::-1])

    return answer




# def cmp(words, querie):
#     n = len(querie)
#     cnt = 0
#     for word in words:
#         if not len_cmp(n, word): continue
#         start = find_start(n, querie)
#         end = find_end(n, querie)
#         if not check_both(querie[start:end + 1], word[start:end + 1]): continue
#         cnt += 1
#     return cnt
#
#
# def check_both(querie, word):
#     if len(querie)!=0:
#         for i in range(len(querie) // 2 + 1):
#             if querie[i] != word[i] or querie[-1 - i] != word[-1 - i]:return False
#         else:return True
#     else:return True
#
#
# def len_cmp(querie_len,word):
#     if querie_len == len(word):
#         return True
#     return False
#
#
# def find_start(querie_len,querie):
#     start=0
#     while querie[start] == "?":
#         start += 1
#         if start == querie_len: break
#     return start
#
#
# def find_end(querie_len,querie):
#     end = querie_len - 1
#     while querie[end] == "?":
#         end -= 1
#         if end==0:break
#     return end
#
#
# def solution(words, queries):
#     answer = []
#     for querie in queries:
#         answer.append(cmp(words,querie))
#     return answer
#
# print(solution(words,queries))