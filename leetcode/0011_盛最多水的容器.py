"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_area, tmp_area = 0, 0
        while(l < r):
            h = 0
            w = r - l
            if height[l] <= height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            tmp_area = h * w
            if max_area < tmp_area:
                max_area = tmp_area
        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


"""
总结：两个指针，断指针移动，另一只指针不动
"""