import sys

def read_int():
    return int(input())

def solve():

    dp = [0] * 251
    dp[0] = 1
    dp[1] = 1   # |
    # || = ㅁ
    # ||| =| ㅁ| , |ㅁ |=
    # |||| =|| ㅁ|| |=| |ㅁ|  , ||ㅁ =ㅁ ㅁㅁ ㅁ= ||= ==

    for i in range(2, 251):
        dp[i] = dp[i-1] + dp[i-2] * 2
    
    while True:
        try:
            N = read_int()
            print(dp[N])
        except:
            break
        
solve()