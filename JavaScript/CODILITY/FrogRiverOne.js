function solution(X, A) {
  const leaves = {}
  let left = X
  let answer = -1
  for (let i=0;i<A.length;i++) {
    if (!leaves[A[i]]) {
      leaves[A[i]] = 1
      left -= 1
      if (left === 0) {
        answer = i
        break
      }
    }
  }
  return answer
}

solution(5,[1,3,1,4,2,3,5,4])