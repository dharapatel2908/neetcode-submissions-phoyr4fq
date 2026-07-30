class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        strings = ''
        def bt(strings,initial,combo):
            if len(strings) == 2*n:
                result.append(strings)
                return
            if initial<n:
                bt(strings+'(',initial +1, combo)
            if initial>combo:
                bt(strings+')',initial,combo+1)
        bt(strings,0,0)
        return result

        