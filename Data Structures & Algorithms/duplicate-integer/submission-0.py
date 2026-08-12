from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= Counter(nums)
        for count in n:
            if n[count]>1:
                return True
        return False
