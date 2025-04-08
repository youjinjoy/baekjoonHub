const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

const N = Number(input[0]);
const arr = input[1].split(' ').map((elem) => Number(elem));

const stack = [];
const answer = Array(N).fill(0);
for (let i = N - 1; i >= 0; i--) {
  if (!stack.length) {
    answer[i] = -1;
    stack.push(i);
    continue;
  }

  if (arr[stack[stack.length - 1]] > arr[i]) {
    answer[i] = arr[stack[stack.length - 1]];
    stack.push(i);
    continue;
  }

  while (stack.length && arr[stack[stack.length - 1]] <= arr[i]) {
    stack.pop();
  }
  if (!stack.length) {
    answer[i] = -1;
  } else {
    answer[i] = arr[stack[stack.length - 1]];
  }
  stack.push(i);
}

console.log(answer.join(' '));
