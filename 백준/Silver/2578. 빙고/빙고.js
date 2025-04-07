const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

// 1. 각 빙고판에 대한 좌표값 저장
const bingoMap = new Map();
for (let i = 0; i < 5; i++) {
  const line = input[i].split(' ');
  for (let j = 0; j < 5; j++) {
    bingoMap.set(line[j], [i, j]);
  }
}

const numbers = [];
for (let i = 5; i < 10; i++) {
  numbers.push(input[i].split(' '));
}

// 2. number 호출될 때마다 해당 좌표값에 대해 rows, columns, diagonals에 추가
// rows, columns, diagonals에 추가하고 값이 5가 됐으면 결과값에 +1
// 결과값이 +3이 되면 해당 numbers의 횟수 출력 (횟수 계속 추적)
let answer = 0;
let result = 0;
const rows = Array(5).fill(0);
const columns = Array(5).fill(0);
const diagonals = Array(2).fill(0); // 0이면 왼쪽&위-오른쪽&아래 대각선
for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    answer += 1;

    const [row, col] = bingoMap.get(numbers[i][j]);

    rows[row] += 1;
    if (rows[row] === 5) {
      result += 1;
    }

    columns[col] += 1;
    if (columns[col] === 5) {
      result += 1;
    }

    if (row === col) {
      diagonals[0] += 1;
      if (diagonals[0] === 5) {
        result += 1;
      }
    }

    if (row + col === 4) {
      diagonals[1] += 1;
      if (diagonals[1] === 5) {
        result += 1;
      }
    }

    if (result >= 3) {
      console.log(answer);
      return;
    }
  }
}
