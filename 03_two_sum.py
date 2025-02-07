from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) >= 2 and len(nums) <= 1000:
            hmap = {}
            for i,n in enumerate(nums):
                diff = target - nums[i]
                if diff not in hmap:
                    hmap[n] = i
                else:
                    return [hmap[diff], i]
                
Sol = Solution()
nums = [3,4,5,6]
target = 7
print(Sol.twoSum(nums, target))