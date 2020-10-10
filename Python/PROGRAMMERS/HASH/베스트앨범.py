def solution(genres, plays):
    albums = dict()

    for i in range(len(genres)):
        if genres[i] not in albums:
            albums[genres[i]] = [plays[i],i,-1]
        else:
            albums[genres[i]][0]+=plays[i]
            if plays[i] > plays[albums[genres[i]][1]]:
                albums[genres[i]][2] = albums[genres[i]][1]
                albums[genres[i]][1] = i
                continue
            if albums[genres[i]][2] == -1:
                albums[genres[i]][2] = i
                continue
            if plays[i] > plays[albums[genres[i]][2]]:
                albums[genres[i]][2] = i
                continue
    ans = sorted(albums.items(),key=lambda x:-x[1][0])
    answer = []
    for element in ans:
        for idx in element[1][1:3]:
            if idx != -1:
                answer.append(idx)

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays =  [500, 600, 150, 800, 2500]

print(solution(genres,plays))