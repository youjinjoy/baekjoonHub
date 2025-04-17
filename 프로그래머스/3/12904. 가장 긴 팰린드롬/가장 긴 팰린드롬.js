function solution(s)
{
    const n = s.length;
    function getLength(left, right) {
        while (left >= 0 && right < n) {
            if (s[left] === s[right]) {
                left -= 1;
                right += 1;
            }
            else {
                break;
            }
        }
        return right - left - 1;
    }
    
    let maxLength = 0;
    for (let i = 0 ; i < n ; i++) {
        maxLength = Math.max(maxLength, getLength(i,i));
        maxLength = Math.max(maxLength, getLength(i,i+1));
    }
    
    return maxLength;
}