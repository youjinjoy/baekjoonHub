const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

const [N, S] = input[0].split(' ').map((value) => parseInt(value));
const numbers = input[1].split(' ').map((value) => parseInt(value));
let count = 0;
function backtrack(sum, start) {
  if (sum.length > 0 && sum.reduce((acc, cur) => acc + cur, 0) === S) {
    count += 1;
  }

  for (let i = start; i < N; i++) {
    sum.push(numbers[i]);
    backtrack(sum, i + 1);
    sum.pop();
  }
}

backtrack([], 0);

console.log(count);
