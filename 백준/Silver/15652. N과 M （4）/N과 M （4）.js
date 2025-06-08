const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
  .readFileSync(path, "utf8")
  .split("\n")
  .map((item) => item.trim());

const [N, M] = input[0].split(" ").map((item) => parseInt(item));
const answer = [];

function backtrack(current, start) {
  if (current.length === M) {
    answer.push(current.join(" "));
    return;
  }

  for (let i = start; i <= N; i++) {
    current.push(i);
    backtrack(current, i);
    current.pop();
  }
}

backtrack([], 1);

console.log(answer.join("\n"));
