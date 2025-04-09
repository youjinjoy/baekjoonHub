const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

// N으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합을 구하는 프로그램을 작성하시오.
// 예를 들어 N=3일 때, 나머지와 몫이 모두 같은 자연수는 4와 8 두 개가 있으므로, 그 합은 12이다.

const N = BigInt(input[0]);

let i = BigInt(0);
let sum = BigInt(0);

while (++i < N) {
  sum += i * N + i;
  // N = 3
  // i = 1 -> 4
  // i = 2 -> 8
}

console.log(sum.toString());
