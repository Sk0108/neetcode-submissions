class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        
        s1_count={}
        for ch in s1:
            s1_count[ch]= s1_count.get(ch,0)+1
        
        window_count= {}
        L= len(s1)
        for i in range(L):
            ch= s2[i]
            window_count[ch]= window_count.get(ch,0)+1
            
        if window_count== s1_count:
            return True

        for i in range(L,len(s2)):
            new_char= s2[i]
            old_char= s2[i-L]
        
            window_count[new_char]=window_count.get(new_char,0)+1
            window_count[old_char]-=1
            if window_count[old_char]==0:
                del window_count[old_char]
            
            if window_count==s1_count:
                return True
        return False
