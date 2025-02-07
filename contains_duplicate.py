#Neetcode Arrays
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_nums = set()
        for i in range(len(nums)):
            if nums[i] in checked_nums:
                return True
            else:
                checked_nums.add(nums[i])
        return False
    
Sol = Solution()
nums = [1, 2, 3, 3]
print(Sol.hasDuplicate(nums))