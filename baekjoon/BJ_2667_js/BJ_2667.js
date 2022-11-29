const filePath = process.platform === "linux" ? "/dev/stdin" : "예제.txt";
const fs = require("fs");

function DFS(row, col) {
  if (row >= 0 && col >= 0 && row < n && col < n) {
    //console.log(row, col)
    if (townMap[row][col] === 1) {
      townMap[row][col] = 0;
      townSize += 1;
      DFS(row + 1, col);
      DFS(row, col + 1);
      DFS(row - 1, col);
      DFS(row, col - 1);
    }
  } else {
    return;
  }
}

let input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = Number(input.shift());
let townMap = input.map((el) => el.trim().split("").map(Number));

// console.log(townMap);
// arr 탐색
let townNum = 0; // 단지 수
let townSize = 0;
const resultTownSize = [];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (townMap[i][j] === 1) {
      DFS(i, j);
      resultTownSize.push(townSize);
      townSize = 0;
      townNum += 1;
    }
  }
}

console.log(townNum);
resultTownSize.sort((a, b) => a - b);
console.log(resultTownSize.join("\n"));
