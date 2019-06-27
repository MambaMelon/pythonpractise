"""
最大子序列的和值
"""

arr = [-2, 1, -3, 4, -1, 2, 1, 3, -5, 4]
dp = [0 for i in range(len(arr))]
dp[0] = arr[0]
m = arr[0]

if len(arr) == 1:
    m = arr[0]
else:
    for i in range(1, len(arr)):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + arr[i]
        else:
            dp[i] = arr[i]

        m = max(m, dp[i])

print(m)