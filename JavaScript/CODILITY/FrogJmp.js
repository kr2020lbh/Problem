function solution(X, Y, D) {
    const toJump = Y-X
    return Math.ceil(toJump/D)
}
console.log(solution(7,21,10))
