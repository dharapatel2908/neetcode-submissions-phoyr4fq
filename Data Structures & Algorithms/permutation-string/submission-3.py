class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case if s1> s2, then it is false
        # Put counter on s1
        # left and right will be on 0th index of the s2
        #right iterate till the window size is same as length of s1
        #then compare the counter of s1 letter and counter of window letter
        #if counter_s1 == counter_window: return True 
        # False: left +=1 from and remove the letter from window of left pointer 
        # in the end of outside of the loop return False
        if len(s1)> len(s2):
            return False
        counter_s1 = Counter(s1) #count of letters of s1
        left =0
        window = defaultdict(int)
        for right in range(len(s2)):
            window[s2[right]] +=1
            while (right-left +1) > len(s1):
                window[s2[left]] -=1
                left +=1
            window_counter = Counter(window)
            if counter_s1 == window_counter:
                return True    
        return False

