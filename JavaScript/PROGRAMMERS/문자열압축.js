function solution(s) {
    let answer = s.length
    let len = 1
    let limit = parseInt(s.length/2) + 1
    while (len < limit ) {
        let idx = 0
        let newS = []
        while (idx < s.length){
            newS.push(s.substring(idx,idx+len))
            idx += len
        }
        if (idx - len < s.length - 1){
            newS.push(s.substring(idx-len,s.length))
        }
        let cnt = 1
        let prevWord = newS[0]
        let newStr = ''
        for (let i=1;i<newS.length;i++) {
            if (newS[i] === prevWord) {
                cnt += 1
            }
            else {
                if (cnt === 1) {
                    newStr += prevWord
                }
                else {
                    newStr += String(cnt) + prevWord
                }
                cnt = 1
            }
            prevWord = newS[i]
        }
        if (answer > newStr.length) {
            answer = newStr.length
            console.log(s,newS,newStr,len)
        }
        len ++
    }
    console.log(answer)
}
// solution("aabbaccc"	)
// solution("ababcdcdababcdcd")
solution("abcabcdede")
// solution("abcabcabcabcdededededede")
// solution("xababcdcdababcdcd")