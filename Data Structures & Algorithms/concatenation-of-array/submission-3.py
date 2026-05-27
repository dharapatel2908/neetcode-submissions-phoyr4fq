class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answers =[]
        for i in range(2):
            for num in nums:
                answers.append(num)
        return answers
        