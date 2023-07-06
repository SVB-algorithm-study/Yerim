class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)

        for s in strs:
            dic["".join(sorted(s))].append(s)
    
        return dic.values()