def solution(files):
    num = '0123456789'
    for i in range(len(files)):
        for j in range(len(files[i])):
            if files[i][j] in num:
                break
        for k in range(j+1,len(files[i])):
            if files[i][k] not in num:
                break
        else:
            k = len(files[i])

        head = files[i][0:j]
        number = files[i][j:k]
        tail = files[i][k::]
            
        files[i] = [head.lower(),head,int(number),number,tail,i]

    sorted_files = sorted(files,key=lambda x:(x[0],x[2],x[-1]))
    answer = [element[1]+element[3]+element[4] for element in sorted_files]

    return answer
# files = ['img12.png', 'img10.png', 'img02.png', 'img2.png', 'img00002.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
# solution(files)
# files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
# solution(files)
solution(['F-15'])
