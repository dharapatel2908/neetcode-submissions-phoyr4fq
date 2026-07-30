class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part =[]
        result = []

        def dfs(i):
            #base case for adding the list into result
            if i>= len(s):
                result.append(part.copy())
                return
            #for checking the palindrome and backtracking
            for j in range(i, len(s)):
                left = i
                right = j
                ok = True
                while left < right:
                    if s[left] != s[right]:
                        ok= False
                        break
                    left , right = left +1, right-1
                if not ok:
                    continue
                    
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()
        dfs(0)
        return result