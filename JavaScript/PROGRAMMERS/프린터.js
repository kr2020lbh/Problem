
function solution(priorities, location) {
    const newPriorities = priorities.map((priority,index)=>{
        return {
            index,
            priority
        }
    })
    
    let cnt = 1
    while(newPriorities.length) {
        const firstElement = newPriorities.shift()
        const isHigest = newPriorities.some(element =>{
            return element.priority > firstElement.priority
        })
        if (isHigest) {
            newPriorities.push(firstElement)
        }
        else {
            if (firstElement.index === location) {
                return cnt
            }
            cnt += 1
        }
    }
}
// function solution(priorities, location) {
//     function checkPrio(prio,newPriorities) {
//         for (let i=0;i<newPriorities.length;i++) {
//             if (newPriorities[i][0] > prio) {
//                 return false
//             }
//         }
//         return true
//     }
    
//     function setNewPrio(priorities) {
//         let idx = 0 
//         const newPriorities = priorities.map(prio => {
//             const element = [prio,idx]
//             idx += 1
//             return element
//         })
//         return newPriorities
//     }

//     const newPriorities = setNewPrio(priorities)
//     let cnt = 1
//     while (true) {
//         const prioElement = newPriorities.shift()
//         const prio = prioElement[0]
//         const idx = prioElement[1]
//         if (!checkPrio(prio,newPriorities)) {
//             newPriorities.push(prioElement)
//         }
//         else {
//             if (idx === location) {
//                 return cnt
//             }
//             cnt += 1
//         }
//     }
// }
console.log(solution([2, 1, 3, 2],2))
console.log(solution([1, 1, 9, 1, 1, 1]	,0))