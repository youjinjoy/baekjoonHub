const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

const [N, M] = input[0].split(' ').map((value) => parseInt(value));

const output = [];

function backtrack(result) {
  if (result.length === M) {
    output.push(result.join(' '));
    return;
  }

  for (let i = 1; i <= N; i++) {
    result.push(i);
    backtrack(result);
    result.pop();
  }
}

backtrack([]);

console.log(output.join('\n'));
