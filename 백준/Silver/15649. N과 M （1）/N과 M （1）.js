const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

const [N, M] = input[0].split(' ').map((value) => parseInt(value));

const visited = Array(N + 1).fill(false);

function backtrack(result) {
  if (result.length === M) {
    console.log(result.join(' '));
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      result.push(i);
      backtrack(result);
      result.pop();
      visited[i] = false;
    }
  }
}

backtrack([]);
