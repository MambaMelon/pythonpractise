"""
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
"""

class Solution(object):
    def isMatch(self, s, p):
        if not p: return not s
        # s 和 p 首位置 匹配, 我们只需比较s的下一位和p 或者p[2:]是否匹配
        if s and len(p) >= 2 and (s[0] == p[0] or p[0] == ".") and p[1] == "*" and (
                    self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:])):
            return True
        # s 和 p 首位置不匹配, 但是p的下个位置是* 所以可以跳到p[2:]
        elif s and len(p) >= 2 and s[0] != p[0] and p[1] == "*" and self.isMatch(s, p[2:]):
            return True
        # s 和 p 首位置匹配, 接着匹配下一个
        elif s and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:]):
            return True
        # 防止s为空 p还剩 ".*" 这种情况
        elif len(p) >= 2 and p[1] == "*" and self.isMatch(s, p[2:]):
            return True
        return False

s = Solution()
print(s.isMatch("abcc", "a.c"))