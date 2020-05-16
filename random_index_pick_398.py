import random
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.__nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = None
        for index, value in enumerate(self.__nums):
            if value == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = index

        return res