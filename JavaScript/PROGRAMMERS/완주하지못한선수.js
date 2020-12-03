function solution(participant, completion) {
    var answer = '';
    const temp = {}
    for (let i=0;i<participant.length;i++){
        if (temp[participant[i]]) {
            temp[participant[i]] += 1
        }
        else {
            temp[participant[i]] = 1
        }
    }
    for (let i=0;i<completion.length;i++) {
        temp[completion[i]] -= 1
    }
    for (let t in temp) {
        if (temp[t]){
            answer = t
            break
        }
    }
    return answer;
}
var participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
var completion = ["josipa", "filipa", "marina", "nikola"]
solution(participant,completion)