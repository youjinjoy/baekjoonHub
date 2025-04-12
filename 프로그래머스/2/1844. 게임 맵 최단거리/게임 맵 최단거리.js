function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    
    const visited = Array.from({length: n}, () => Array(m).fill(false));
    visited[0][0] = true;
    
    const queue = [[0,0,1]];    
    let head = 0;
    
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];

    while (head < queue.length) {

        const [cx, cy, step] = queue[head++];
       
        for (let i = 0 ; i < 4 ; i++) {
            const [nx, ny] = [cx+dx[i], cy+dy[i]];
             if (nx === n - 1 && ny === m - 1) {
                return step + 1;
            }

            const isInside = 0 <= nx && nx < n && 0 <= ny && ny < m;

            if (isInside && maps[nx][ny] === 1 && !visited[nx][ny]) {
                visited[nx][ny] = true;
                queue.push([nx, ny, step + 1]);
            }
        }
    }
    
    return -1;
}