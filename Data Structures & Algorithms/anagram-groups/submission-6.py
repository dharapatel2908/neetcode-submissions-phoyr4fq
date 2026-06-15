class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sort = ''.join(sorted(s))
            result[sort].append(s)
        return list(result.values())