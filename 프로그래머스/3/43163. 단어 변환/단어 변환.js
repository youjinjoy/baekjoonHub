function solution(begin, target, words) {

    // 초기 조건
    const wordSet = new Set(words);
    if (!wordSet.has(target)) {
        return 0;
    }
    
    const n = words.length;
    const m = words[0].length;
    const visited = Array(n).fill(false);
    
    let answer = 0;
    function dfs(current, depth) {
        if (current === target) {
            answer = depth;
            return;
        }
        
        for (let i = 0 ; i < n ; i++) {
            const convertable = getDuplicatedCount(current, words[i]) === m - 1;

            if (!visited[i] && convertable) {
                visited[i] = true;
                dfs(words[i], depth+1);
                visited[i] = false;
            }
        }
    }
    
    dfs(begin, 0);
    return answer;
}

function getDuplicatedCount(a, b) {
    const n = a.length;
    let pointer = 0;
    let count = 0;
    
    while (pointer < n) {
        if (a[pointer] === b[pointer]) {
            count += 1;
        }
        pointer += 1;
    }
    
    return count;
}