class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorts = "".join(sorted(s))
            result[sorts].append(s)
        return list(result.values())