class Solution(object):

    def bisect_left(self, a, x, lo, hi):

        while lo < hi:
            mid = (lo + hi)//2
            if x > a[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def bisect_right(self, a, x, lo, hi):
        while lo < hi:
            mid = (lo + hi)//2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1

        return lo

    def count(self, arr, target):
        n = len(arr)
        left = self.bisect_left(arr, target, 0, n)
        right = self.bisect_right(arr, target, left, n)
        return right - left