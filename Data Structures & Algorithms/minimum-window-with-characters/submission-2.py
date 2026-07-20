class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count= Counter(t)
        window = {}
        have,need =0,len(t_count)
        result =[float("inf"),0,0]

        left =0
        for right in range(len(s)):
            char= s[right]
            window[char] = window.get(char,0)+1

            if char in t_count and window[char]==t_count[char]:
                have+=1
            while have==need:
                if (right-left+1) <result[0]:
                    result =[right-left+1,left,right]
                window[s[left]] -=1
                if s[left] in t_count and window[s[left]]<t_count[s[left]]:
                    have-=1
                left+=1
        
        _,l,r = result
        return s[l:r+1] if result[0] != float("inf") else ""
