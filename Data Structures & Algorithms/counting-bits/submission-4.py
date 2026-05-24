class Solution:
    def countBits(self, n: int) -> List[int]:
        output =[]
        for i in range(0,n+1):
            count = i.bit_count()
            output.append(count)
        return output