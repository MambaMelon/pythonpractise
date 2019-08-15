"""
输入: s = "LEETCODEISHIRING", numRows = 3
    L   C   I   R
    E T O E S I I G
    E   D   H   N
输出: "LCIRETOESIIGEDHN"
"""

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = min(len(s), numRows)
        DecDict = {}
        for row in range(rows):
            DecDict[row] = []

        curRow = 0
        goingDown = False

        for c in s:
            DecDict[curRow].extend(c)
            if curRow==0 or curRow==numRows-1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        retS = ''.join([''.join(val) for val in DecDict.values()])
        return retS

s = Solution()
res = s.convert("LEETCODEISHIRING", 3)
print(res)
