"""
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        left = 0
        right = 0
        for i in range(n-2, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n, 1):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and right - left<j - i:
                    left = i
                    right = j

        return s[left:right+1]


s = Solution()
res = s.longestPalindrome("babad")
print(res)