import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_counter = collections.Counter(s1)

        window_counter = collections.Counter()

        for i, c in enumerate(s2):
            window_counter[c] += 1

            if i >= len(s1):
                left_elem = s2[i - len(s1)]
                if window_counter[left_elem] == 1:
                    del window_counter[left_elem]
                else:
                    window_counter[left_elem] -= 1

            if window_counter == s1_counter:
                return True

        return False