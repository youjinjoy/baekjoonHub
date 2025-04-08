function solution(s)
{
    function getPalindromeLength(left, right){
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left -= 1;
            right += 1;
        }
        return right - left - 1;
    }
    
    let evenLen = 1;
    let oddLen = 1;
    for (let i = 0 ; i < s.length ; i++) {
        evenLen = Math.max(evenLen, getPalindromeLength(i, i));
        oddLen = Math.max(oddLen, getPalindromeLength(i, i + 1));
    }
    return Math.max(evenLen, oddLen);
}