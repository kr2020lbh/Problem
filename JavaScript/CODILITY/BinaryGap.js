
function integer2Bin(N) {
    if (N < 2) {
        if (N == 1) {
            return '1' 
        }
        else {
            return '0'
        }
    }
    else {
        return String(N%2) + integer2Bin(parseInt(N/2))
    }
}
function solution(N) {
    let answer = 0
    const binary = integer2Bin(N).split("").reverse().join("")
    const splitedBin = binary.split("1")
    console.log(binary)
    console.log(splitedBin)
    for (let i=0;i<splitedBin.length;i++) {
        if (i===0 || i===splitedBin.length-1) {
            continue
        }
        if (splitedBin[i]) {
            if (splitedBin[i].length > answer) {
                answer = splitedBin[i].length
            }
        }
    }
    return answer
}

solution(32)
