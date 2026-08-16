class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_str= set()
        l=0
        max_len=0
        for r in range(len(s)):
            while s[r] in longest_str:
                longest_str.remove(s[l])
                l+=1
            longest_str.add(s[r])
            max_len= max(max_len, r-l+1)
        return max_len