import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        counter_s = collections.Counter(s[:len(p) - 1])
        counter_p = collections.Counter(p)
        res = []
        for i in range(len(p) - 1, len(s)):
            counter_s[s[i]] += 1
            if counter_s == counter_p:
                res.append(i - (len(p) - 1))
            counter_s[s[i - (len(p) - 1)]] -= 1
            if counter_s[s[i - (len(p) - 1)]] == 0:
                del counter_s[s[i - (len(p) - 1)]]

        return res