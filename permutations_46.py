    from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        permutations = deque()
        permutations.append([])

        for num in nums:
            n = len(permutations)


            permutations.
            for _ in range(n):
                old_permutation = permutations.popleft()
                for i in range(len(old_permutation) + 1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(i, num)
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    else:
                        permutations.append(new_permutation)

        return result

    def permutation_2
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break
            ans = new_ans
        return ans