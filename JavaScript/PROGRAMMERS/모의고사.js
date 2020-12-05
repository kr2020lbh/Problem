function solution(answers) {
    var studensts = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5],
    ]
    var indexes = [0,0,0]
    var answer = [[0,1],[0,2],[0,3]];
    for (let i=0;i<answers.length;i++) {
        var ans = answers[i]
        for (let j=0;j<3;j++) {
            if (ans === studensts[j][indexes[j]]) answer[j][0] += 1
            indexes[j] = (indexes[j]+1) % studensts[j].length
        }
      
    }
    answer.sort((a,b) =>{
        return b[0]-a[0]
    })
    var res = []
    answer.forEach(element => {
        if (answer[0][0] === element[0]) res.push(element[1])
    })
    return res
}

// function solution(answers) {
//     var answer = [];
//     var a1 = [1, 2, 3, 4, 5];
//     var a2 = [2, 1, 2, 3, 2, 4, 2, 5]
//     var a3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

//     var a1c = answers.filter((a,i)=> a === a1[i%a1.length]).length;
//     var a2c = answers.filter((a,i)=> a === a2[i%a2.length]).length;
//     var a3c = answers.filter((a,i)=> a === a3[i%a3.length]).length;
//     var max = Math.max(a1c,a2c,a3c);

//     if (a1c === max) {answer.push(1)};
//     if (a2c === max) {answer.push(2)};
//     if (a3c === max) {answer.push(3)};


//     return answer;
// }
solution([3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,3,3,4,4,5,5])