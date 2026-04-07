from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int):
        prevHash = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash[num] = i
        return


nums = [2, 7, 11, 15]
target = 9

s = Solution()
result = s.two_sum(nums, target)
print(result)
