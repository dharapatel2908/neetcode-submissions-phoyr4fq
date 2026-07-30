class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result =[]
        hashmap = {"2":"abc","3":"def","4":"ghi",
        "5":"jkl","6":"mno","7":"pqrs",
        "8":"tuv","9":"wxyz"}
        strings=""
        def backtrack(i,strings):
            if len(strings) == len(digits):
                result.append(strings)
                return
            for c in hashmap[digits[i]]:
                backtrack(i+1,strings+c)

        if digits:
            backtrack(0,strings)
        return result            