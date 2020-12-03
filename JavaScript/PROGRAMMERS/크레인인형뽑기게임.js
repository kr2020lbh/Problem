function solution(board, moves) {
  var box = []
  var answer = 0;
  var rowLimit = board.length

  for (let i=0;i<moves.length;i++){

    var col = moves[i] - 1

    for (let row=0;row<rowLimit;row++){
      var boardValue = board[row][col]
      if (boardValue !== 0){
        box.push(boardValue)
        board[row][col] = 0
        var boxLength =box.length
        if (boxLength >= 2){
          if (box[boxLength-1] === box[boxLength-2]){
            box.splice(boxLength-2,2)
            answer += 2
          }
        }
        break
      }
    }
  }
  return answer;
}
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	,[1,5,3,5,1,2,1,4])