words = []
for i in range(26):
    words.append(chr(97+i))
words+=words
def solution(encrypted_text, key, rotation):
    encrypted_text = list(encrypted_text)

    rotation = -1*rotation
    rotation = rotation % len(encrypted_text)
    if rotation > 0:
        encrypted_text =encrypted_text[len(encrypted_text)-rotation:len(encrypted_text)] + encrypted_text[0:len(encrypted_text)-rotation]
    if rotation < 0:
        encrypted_text = encrypted_text[rotation:len(encrypted_text)] + encrypted_text[0:rotation]
    for i in range(len(encrypted_text)):
        num = ord(encrypted_text[i]) - 97 - (ord(key[i]) - 96)
        if num < 0:
            num += 26
        encrypted_text[i] = words[num]
    return ''.join(encrypted_text)

solution("aaaaaaaaaaaaaaaaaaaaaaaaaa","abcdefghijklmnopqrstuvwxyz",0)
# solution("hellopython","abcdefghijk",3)
solution("qyyigoptvfb","abcdefghijk",-1)
solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",-1000)
solution('a','a',0)
solution('a','b',3)
solution('z','z',3)
#
# print(ord('a'),ord('z'))
# words_dict = dict()
# words = []
# for i in range(26):
#     words_dict[(chr(97+i))] = i
#     words.append((chr(97+i)))
# print(words_dict,words)
# def solution(encrypted_text, key, rotation):
#     length = len(encrypted_text)
#
#     rotation = -1*rotation
#     rotation = rotation % len(encrypted_text)
#
#     if rotation > 0:
#         encrypted_text=encrypted_text[len(encrypted_text)-rotation:len(encrypted_text)] + encrypted_text[0:len(encrypted_text)-rotation]
#
#     if rotation < 0:
#         encrypted_text=encrypted_text[rotation:len(encrypted_text)] + encrypted_text[0:rotation]
#     original_text = []
#     for i in range(length):
#         enc_num = words_dict[encrypted_text[i]]
#         key_num = words_dict[key[i]] + 1
#         num = enc_num - key_num
#         if num < 0:
#             num += 26
#         original_text.append(words[num])
#
#     return ''.join(original_text)
#
#
# solution("qyyigoptvfb","abcdefghijk",3)
# for i in range(-1000,1001,1):
#     solution("qyyigoptvfb", "abcdefghijk", i)
print(-3%1000)