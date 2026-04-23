class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            sortedstr = ''.join(sorted(s))
            dic[sortedstr].append(s)
        return list(dic.values())