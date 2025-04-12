function solution(n, computers) {
    let edges = 0;
    const visited = Array(n).fill(0);
    const graph = Array.from({length: n}, () => Array(0));
    
    for (let i = 0 ; i < n ; i++) {
        for (let j = i + 1 ; j < n ; j++) {
            if (computers[i][j] === 1) {
                graph[i].push(j);
                graph[j].push(i);
            }
        }
    }
    
    function dfs(cur) {        
        visited[cur] = true;
        for (const next of graph[cur]) {
            if (!visited[next]) {
                dfs(next);
                edges += 1;
            }
        }
    }
    
    for (let i = 0 ; i < n ; i++) {
        if (!visited[i]) {
            dfs(i);                
        }
    }
    
    return n - edges;
}