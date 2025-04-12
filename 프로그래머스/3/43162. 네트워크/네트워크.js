function solution(n, computers) {
    // computers 로부터 연결된 edges 추출
    const edges = [];
    for (let i = 0 ; i < computers.length ; i++) {
        for (let j = i + 1 ; j < computers[0].length ; j++) {
            if (computers[i][j] === 1) {
                edges.push([i,j]);                
            }
        }
    }
    // edges 기반으로 그룹 개수 세기
    const N = computers.length;
    const parent = Array.from({length: N}, (_, index) => index)
    
    function find(x) {
        if (x !== parent[x]) {
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
    
    for (const [x,y] of edges) {
        union(x,y);        
    }
    
    const group = new Set();
    for (let i = 0 ; i < N ; i++) {
        group.add(find(parent[i]));
    }
    
    return group.size;
}