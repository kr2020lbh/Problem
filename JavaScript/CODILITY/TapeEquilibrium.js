function solution(A) {
    let sumPart1 = A[0]
    let sumPart2 = 0
    for (let i=1;i<A.length;i++) {
        sumPart2 += A[i]
    }
    let minDiff = Math.abs(sumPart1-sumPart2)
    for (let i=1;i<A.length-1;i++) {
        sumPart1 += A[i]
        sumPart2 -= A[i]
        const tmpDiff = Math.abs(sumPart1-sumPart2)
        if (minDiff > tmpDiff) {
            minDiff = tmpDiff
        }
    }
    return minDiff
}

solution([3,1,2,4,3])