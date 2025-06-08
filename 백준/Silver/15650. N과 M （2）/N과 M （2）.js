const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
  .readFileSync(path, "utf8")
  .split("\n")
  .map((item) => item.trim());

const [N, M] = input[0].split(" ").map((item) => parseInt(item));

const visited = Array(M + 1).fill(false);

function backtrack(current, start) {
  if (current.length === M) {
    console.log(current.join(" "));
    return;
  }

  for (let i = start; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      current.push(i);
      backtrack(current, i + 1);
      current.pop();
      visited[i] = false;
    }
  }
}

backtrack([], 1);
