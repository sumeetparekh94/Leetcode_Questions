class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in map:
                map[diff] = i
            else:
                res.append(map[nums[i]])
                res.append(i)

        return res