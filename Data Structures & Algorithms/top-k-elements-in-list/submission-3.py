class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number = Counter(nums)
        num=number.most_common(k)
        ml = list()
        for x,_ in num:
            ml.append(x)
        return ml