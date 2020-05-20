import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = collections.defaultdict(list)

        for s in strs:
            dict_anagrams[tuple(sorted(s))].append(s)

        return list(dict_anagrams.values())