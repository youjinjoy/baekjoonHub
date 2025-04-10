const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((line) => line.trim());

const [V, E] = input[0].split(' ').map((value) => parseInt(value));
const edges = [];
for (let i = 1; i <= E; i++) {
  edges.push(input[i].split(' ').map((value) => parseInt(value)));
}

const parent = Array.from({ length: V + 1 }, (_, index) => index);

function find(x) {
  if (parent[x] !== x) {
    parent[x] = find(parent[x]);
  }
  return parent[x];
}

function union(x, y) {
  const rootX = find(x);
  const rootY = find(y);
  if (rootX === rootY) {
    return false;
  }
  parent[rootY] = rootX;
  return true;
}

edges.sort((a, b) => a[2] - b[2]);

let cost = 0;
for (const [x, y, c] of edges) {
  if (union(x, y)) {
    cost += c;
  }
}

console.log(cost);
