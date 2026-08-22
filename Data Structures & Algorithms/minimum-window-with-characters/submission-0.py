class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        
        t_count= {}
        for ch in t:
            t_count[ch]= t_count.get(ch,0)+1
        
        window_count= {}
        have, need= 0, len(t_count)
        result= ""
        result_len= float('inf')
        left=0
        for right in range(len(s)):
            ch= s[right]
            window_count[ch]= window_count.get(ch,0)+1

            if ch in t_count and window_count[ch] == t_count[ch]:
                have+=1
            
            while have==need:
                if (right-left+1)< result_len:
                    result= s[left:right +1]
                    result_len= right-left+1
                left_char= s[left]
                window_count[left_char]-=1
                if left_char in t_count and window_count[left_char]< t_count[left_char]:
                    have-=1
                
                left+=1
        return result
