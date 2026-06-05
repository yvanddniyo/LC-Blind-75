from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int):
        obj = {}
        for index, num in enumerate(nums):
            print("print", obj)
            diff = target - num
            if diff in obj:
                return [obj[diff], index]
            else:
                obj[num] = index
        return


nums = [2, 7, 11, 15]
target = 18

s = Solution()
result = s.two_sum(nums, target)
print("->", result)
