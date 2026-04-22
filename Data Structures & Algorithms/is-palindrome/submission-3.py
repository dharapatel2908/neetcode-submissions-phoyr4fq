class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(c):
            return ((c>="a" and c<='z')
            or (c>="A" and c<='Z')
            or (c>="0" and c<='9'))

        # Ambiguity = Spacing, numbers, special characters, case sensitive
        left = 0
        right = len(s) -1
        while left <= right:
            if not check(s[left]):
                left +=1
                continue
            elif not check(s[right]):
                right -=1
                continue
            elif s[left].lower() == s[right].lower():
                left +=1
                right -=1
            else:
                return False
        return True
            