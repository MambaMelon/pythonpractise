"""
输入: 123
输出: 321

输入: -123
输出: -321

输入: 120
输出: 21
"""

import math

class Solution:
    def reverse(self, x):
        if x < 0:
            s= str(abs(x))[::-1]
            res = -int(s)
        else:
            s = str(x)[::-1]
            res = int(s)

        if res < -math.pow(2, 31) or res > math.pow(2, 31)-1:
            res = 0
            return res


s = Solution()
print(s.reverse(-1230))
