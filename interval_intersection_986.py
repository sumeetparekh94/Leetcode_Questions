class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        start = 0
        end = 1
        res = []

        while i < len(A) and j < len(B):

            a_overlaps_b = A[i][start] >= B[j][start] and A[i][start] <= B[j][end]

            b_overlaps_a = B[j][start] >= A[i][start] and B[j][start] <= A[i][end]

            if a_overlaps_b or b_overlaps_a:
                new_interval = [0, 0]
                new_interval[start] = max(A[i][start], B[j][start])
                new_interval[end] = min(A[i][end], B[j][end])
                res.append(new_interval)

            if A[i][end] < B[j][end]:
                i += 1
            else:
                j += 1

        return res
