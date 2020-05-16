class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        char_map = {}
        max_len = 0
        window_start = 0

        for i in range(len(s)):
            if s[i] in char_map and window_start <= char_map[s[i]]:
                window_start = char_map[s[i]] + 1

            else:
                max_len = max(max_len, i - window_start + 1)

            char_map[s[i]] = i

        return max_len