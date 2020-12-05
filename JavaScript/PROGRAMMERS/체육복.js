function solution(n, lost, reserve) {
    var answer = n;
    var students = []
    for(let i=0;i<n;i++) students.push(1)
    for(let i=0;i<reserve.length;i++) {
        var r = reserve[i]
        students[r-1] = 2
    }
    for(let i=0;i<lost.length;i++) {
        var l = lost[i]
        students[l-1] -= 1
        if (students[l-1] === 0) answer -= 1
    }
    for(let i=0;i<n;i++) {
        if (students[i] === 0) {
            if (0<i && i < n) {
                if (students[i-1] === 2) {
                    students[i] = 1
                    students[i-1] = 1
                    answer += 1
                    continue
                }
                if (students[i+1] === 2) {
                    students[i] = 1
                    students[i+1] = 1
                    answer += 1
                    
                }
            }
            if (i===0) {
                if (students[i+1] === 2) {
                    students[i+1] = 1
                    students[i] = 1
                    answer += 1
                }
            }
            if (i===n-1) {
                if (students[i-1] === 2) {
                    students[i-1] = 1
                    students[i] = 1
                    answer += 1
                }
            }
        }

    }
    console.log(answer,students)
    return answer;
}
solution(5,[2,3],[1,2])