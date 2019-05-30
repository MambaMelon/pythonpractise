
'''
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if nums[i] in d.keys():
                return d[nums[i]], i
            else:
                d[t] = i


s = Solution()

nums = [2, 7, 11, 15]
target = 9

res = s.twoSum(nums, target)

print(res)