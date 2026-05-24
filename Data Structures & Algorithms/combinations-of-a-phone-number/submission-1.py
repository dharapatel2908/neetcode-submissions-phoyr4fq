class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        hashmap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
            "7":"pqrs","8":"tuv","9":"wxyz"}

        def backtracking(i,string):
            if len(string) ==len(digits):
                result.append(string)
                return
            for c in hashmap[digits[i]]:
                backtracking(i+1,string+c)
        if digits:
            backtracking(0,"")
        return result