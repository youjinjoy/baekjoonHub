const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
  .readFileSync(path, "utf8")
  .split("\n")
  .map((item) => item.trim());

const [N, M] = input[0].split(" ").map((item) => parseInt(item));

const numbers = input[1].split(" ").map((item) => parseInt(item));
numbers.sort((a, b) => a - b);

const answer = [];
const visited = Array(M).fill(false);
function bactrack(current) {
  if (current.length === M) {
    answer.push(current.join(" "));
    return;
  }

  for (let i = 0; i < N; i++) {
    if (visited[i]) {
      continue;
    }

    if (i > 0 && numbers[i] === numbers[i - 1] && !visited[i - 1]) {
      continue;
    }

    visited[i] = true;
    current.push(numbers[i]);
    bactrack(current);
    current.pop();
    visited[i] = false;
  }
}

bactrack([]);
console.log(answer.join("\n"));
