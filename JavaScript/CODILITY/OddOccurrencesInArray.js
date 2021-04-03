
function solution(A) {
    const check = {}
    A.forEach(element => {
        if (check[element]) {
            check[element] += 1
            if (check[element] === 2) {
                delete check[element]
            }
        }
        else {
            check[element] = 1
        }
    });
    console.log(check)
    return parseInt(Object.keys(check))
}
solution([9,3,9,3,9,7,9])
