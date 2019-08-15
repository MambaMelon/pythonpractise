"""
输入: 121
输出: true
"""

class Solution:
    def isPalindrome(self, x):

        reverse_temp = 0
        while x > reverse_temp:
            reverse_temp = reverse_temp * 10 + x % 10
            x = x // 10

        return x == reverse_temp or x == reverse_temp // 10
s = Solution()
print(s.isPalindrome(123221))
