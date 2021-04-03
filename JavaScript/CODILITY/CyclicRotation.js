
function solution(A, K) {
    K%=A.length
    for (let i=0;i<K;i++) {
        A.unshift(A.pop())
    }
    return A
}
for(let i=0;i<4;i++) {
    solution([1, 2, 3, 4],i)
}