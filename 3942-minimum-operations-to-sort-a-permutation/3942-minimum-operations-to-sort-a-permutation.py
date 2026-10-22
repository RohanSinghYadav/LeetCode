class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        p = nums.index(0)

        forward = True
        backward = True

        for j in range(n):
            if nums[(p + j) % n] != j:
                forward = False
            if nums[(p - j) % n] != j:
                backward = False

            if not forward and not backward:
                return -1

        ans = float('inf')

        if forward:
            ans = min(p, n - p + 2)

        if backward:
            b = n - 1 - p
            ans = min(ans, b + 1, n - b + 1)

        return ans