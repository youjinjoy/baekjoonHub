function solution(numbers, target) {
    let count = 0;
    
    function dfs(result, depth) {
        if (depth >= numbers.length) {
            if (result === target) {
                count += 1;
            }
            return;
        }
        
        dfs(result + numbers[depth], depth + 1);
        dfs(result - numbers[depth], depth + 1);
    }
    
    dfs(0,0);

    return count;
}