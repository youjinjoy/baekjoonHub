import sys
input = sys.stdin.readline

tc = int(input())


def calc_dp(arr):
    for i in range(2, len(arr)):
        arr[i] = arr[i-1] + arr[i-2]


zeros = [0 for _ in range(41)]
zeros[0], zeros[1] = 1, 0

ones = [0 for _ in range(41)]
ones[0], ones[1] = 0, 1

calc_dp(zeros)

calc_dp(ones)

answer = []
for _ in range(tc):
    n = int(input())
    answer.append((zeros[n], ones[n]))

for item in answer:
    print(*item)
