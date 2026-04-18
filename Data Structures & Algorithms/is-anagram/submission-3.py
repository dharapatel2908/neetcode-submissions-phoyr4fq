class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_s = Counter(s)
        str_t = Counter(t)
        if str_s == str_t:
            return True
        else:
            return False