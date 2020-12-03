// function solution(numbers) {
//   var numberResult = new Array(201)
//   var numbersLength = numbers.length
//   for (let i=0;i<numbersLength-1;i++) {
//     for (let j=i+1;j<numbersLength;j++) {
//       numberResult[numbers[i]+numbers[j]] = 1
//     }
//   }
//   var answer = []
//   for (let i=0;i<numberResult.length;i++) {
//     if (numberResult[i]) {
//       answer.push(i)
//     }
//   }
//   console.log(answer)
//   return answer
// }



function solution(numbers) {
    const temp = []

    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            temp.push(numbers[i] + numbers[j])
        }
    }
    console.log(temp)
    console.log(new Set(temp))
    const answer = [...new Set(temp)]

    return answer.sort((a, b) => a - b)
}

solution([5,0,2,7])