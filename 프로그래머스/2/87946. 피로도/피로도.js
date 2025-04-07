function solution(k, dungeons) {
    let maxCount = 0;
    const visited = Array(dungeons.length).fill(false);
    
    function backtrack(fatigue, count) {
        maxCount = Math.max(maxCount, count);
        
        for (let i = 0; i < dungeons.length ; i++) {
            
            if (!visited[i] && fatigue >= dungeons[i][0]) {
                visited[i] = true;
                backtrack(fatigue-dungeons[i][1], count+1);
                visited[i] = false;
            }
            
        }
    }
    
    backtrack(k, 0);
    
    return maxCount;
}