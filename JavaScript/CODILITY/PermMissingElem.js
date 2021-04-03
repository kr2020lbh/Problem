function solution(A) {
    const check = {}
    for (let i=1;i<A.length+2;i++) {
        check[i] = 1
    }
    A.forEach(el => {
        if(check[el]) {
            delete check[el]
        }
    })
    return parseInt(Object.keys(check))
}
solution([1,2,3,5])