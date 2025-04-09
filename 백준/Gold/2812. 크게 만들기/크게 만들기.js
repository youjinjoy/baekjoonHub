const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

const [N, K] = input[0].split(' ').map((elem) => Number(elem));
const numbers = input[1].split('').map((elem) => Number(elem));

const stack = [];
let removable = K;

for (let i = 0; i < N; i++) {
  if (!stack.length) {
    stack.push(numbers[i]);
    continue;
  }

  while (numbers[i] > stack[stack.length - 1] && removable > 0) {
    stack.pop();
    removable -= 1;
  }
  stack.push(numbers[i]);
}

while (stack.length > N - K) {
  stack.pop();
}

console.log(stack.join(''));
