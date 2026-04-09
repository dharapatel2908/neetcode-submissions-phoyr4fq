class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number = Counter(nums)
        num=number.most_common(k)
        return [x for x,_ in num]