import re
def solution(word,pages):
    scores = {}
    meta_pattern = '<meta.*content="https://(.*)"/>'
    url_pattern = '<a.*href="https://(.*)">'
    for i in range(len(pages)):
        page = pages[i]
        meta_link = re.search(meta_pattern,page).group(1)
        url_links = re.findall(url_pattern,page)
        basic_socre = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())

        scores[meta_link] = [i, 0, [], 0, 0]  # 인덱스, 기본점수, 외부링크, 외부링크 수, 링크점수
        scores[meta_link][2] = list(set(url_links))
        scores[meta_link][1] = basic_socre
        scores[meta_link][3] = len(list(set(url_links)))

    for idx, basic, links, links_length, link_score in scores.values():
        for link in links:
            if scores.get(link):
                scores[link][-1] += basic/links_length
    new_score = []
    for idx,basic,links,links_length,link_score in scores.values():
        new_score.append([idx,basic + link_score])
    answer = sorted(new_score,key=lambda x : (-x[1],x[0]))[0][0]
    return answer
# def solution(word, pages):
#     meta_pattern = re.compile('<meta.*content')
#     word = word.lower()
#     word_pattern = '(?=([^a-z^A-Z]{w}[^a-z^A-Z]))|(?=(^{w}[^a-z^A-Z]))|(?=([^a-z^A-Z]{w}$))'.format(w=word)
#     scores = {}
#     for i in range(len(pages)):
#         page = pages[i]
#         print(re.findall('<a href="https:.[^"]*"', page))
#         lines = page.split('\n')
#         meta_url = ''
#         for j in range(len(lines)):
#             line = lines[j].strip()
#             if meta_url == '' and meta_pattern.match(line):
#                 meta_url = re.search('https://.*"',line).group()[8:-1]
#                 scores[meta_url] = [i,0,[],0,0] # 인덱스, 기본점수, 외부링크, 외부링크 수, 링크점수
#             if (re.search('<a.*">',line)):
#                 a_tag = (re.search('<a.*">',line).group())
#                 link = re.search('https.*"',a_tag).group()[8:-1]
#                 scores[meta_url][2].append(link)
#                 scores[meta_url][3] += 1
#             if line:
#                 cnt = (len(re.findall(word_pattern,line,re.I)))
#                 if cnt:
#                     scores[meta_url][1] += cnt
#     for key,val in scores.items():
#         idx,basic,links,links_length,link_score = val
#         for link in links:
#             if scores.get(link):
#                 scores[link][-1] += basic/links_length
#     new_score = []
#     for idx,basic,links,links_length,link_score in scores.values():
#         new_score.append([idx,basic + link_score])
#     answer = sorted(new_score,key=lambda x : (-x[1],x[0]))[0][0]
#     return answer

word = 'blind'
pages1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
pages2 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
pages3 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#0muzi0muzi0!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
solution(word,pages1)
solution('Muzi',pages2)
solution('Muzi',pages3)