from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        window_start = 0
        max_len = 0

        for i in range(len(A)):
            if A[i] == 0 and K:
                K -= 1

            elif A[i] == 0:
                while A[window_start] != 0:
                    window_start += 1
                window_start += 1

            max_len = max(max_len, i - window_start + 1)

        return max_len



