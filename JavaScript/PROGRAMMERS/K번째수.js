// function solution(array, commands) {
//     var answer = []

//     for (let i=0;i<commands.length;i++) {
//          var idx1 = commands[i][0]
//          var idx2 = commands[i][1]
//          var idx3 = commands[i][2]
//          var tmpArray = []
//          for (let j=idx1-1;j<idx2;j++) {
//             tmpArray.push(array[j])
//          }
//          tmpArray = tmpArray.sort((a,b) => {
//              return a-b
//          })
//          answer.push(tmpArray[idx3-1])
//     }
//     return answer
// }

function solution(array, commands) {
    return commands.map(command => {
        var [sIdx,eIdx,idx] = command
        var tmpArray = []
        for (let j=sIdx-1;j<eIdx;j++) {
           tmpArray.push(array[j])
        }
        return tmpArray.sort( (a,b) => {return a-b} )[idx-1]
    })
}
var a= solution([1, 5, 2, 6, 3, 7, 4]	,[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	)
console.log(a)