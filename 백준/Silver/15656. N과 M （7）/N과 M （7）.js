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
function bactrack(current) {
  if (current.length === M) {
    answer.push(current.join(" "));
    return;
  }

  for (let i = 0; i < N; i++) {
    current.push(numbers[i]);
    bactrack(current);
    current.pop();
  }
}

bactrack([], 0);
console.log(answer.join("\n"));
