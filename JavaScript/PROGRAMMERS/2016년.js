function solution(a, b) {
    a -= 1 
    b -= 1
    var month = [31,29,31,30,31,30,31,31,30,31,30]
    var day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    var days = b
    for (let i=0;i<a;i++) {
        days += month[i]
    }
    return day[(days)%7]
}
var month = [31,28,31,30,31,30,31,31,30,31,30,31]

for (let i=1;i<=12;i++) {
    for (let j=1;j<=month[i-1];j++) {
        console.log(i,j,solution(i,j))
    }
}