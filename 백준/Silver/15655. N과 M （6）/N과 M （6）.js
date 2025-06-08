const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
  .readFileSync(path, "utf8")
  .split("\n")
  .map((item) => item.trim());

const [N, M] = input[0].split(" ").map((item) => parseInt(item));

const numbers = input[1].split(" ").map((item) => parseInt(item));
numbers.sort((a, b) => a - b);

const visited = Array(M).fill(false);
const answer = [];
function bactrack(current, start) {
  if (current.length === M) {
    answer.push(current.join(" "));
    return;
  }

  for (let i = start; i < N; i++) {
    visited[i] = true;
    current.push(numbers[i]);
    bactrack(current, i + 1);
    current.pop();
    visited[i] = false;
  }
}

bactrack([], 0);
console.log(answer.join("\n"));
