class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        current = 1
        for i in range(1,len(nums)):
            if nums[i]== nums[i-1]:
                continue
            elif nums[i]== nums[i-1]+ 1:
                current+=1
            else:
                current= 1
            max_len= max(max_len, current)
        return max_len