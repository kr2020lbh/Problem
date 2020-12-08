function solution(n) {
    var tmp = n
    var tmpString = ''
    while (tmp > 0) {
        tmpString += String(tmp%3)
        tmp = parseInt(tmp/3)
    }
    var numbers = tmpString.split("")
    var answer = 0;
    for (let i=0;i<numbers.length;i++) {
        answer += Math.pow(3,i) * numbers[ numbers.length - 1 - i] 
    }
    return answer;
}
solution(45)
var n = 32
console.log(n.toString(2).split("").reverse().join(""))
console.log(typeof(n.toString(2)))