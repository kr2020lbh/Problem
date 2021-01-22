function solution(bridge_length, weight, truck_weights) {
    
    function setArray(arrayLength) {
        const Q = []
        for(let i=0;i<arrayLength;i++) {
            Q.push(0)
        }
        return Q
    }
    
    let idx = 0;
    const Q = setArray(bridge_length);
    let sumOfQ = 0;
    let time = 0;
    
    while (idx<truck_weights.length) {
        const firstElement = Q.shift()
        sumOfQ -= firstElement
        const cur = truck_weights[idx]
        if (cur + sumOfQ <weight) {
            Q.push(cur)
            sumOfQ += cur
            idx += 1
        }
        else {
            Q.push(0)
        }
        time += 1
    }
    return time+bridge_length
}

console.log(solution(2,10,	[7,4,5,6]))