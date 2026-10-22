class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        def get_shift(arr):
            shift = arr.index(0)

            for j in range(n):
                if arr[(shift + j) % n] != j:
                    return -1

            return shift

        a = get_shift(nums)
        b = get_shift(nums[::-1])

        ans = float('inf')

        if a != -1:
            ans = min(ans, a, n - a + 2)

        if b != -1:
            ans = min(ans, b + 1, n - b + 1)

        return ans if ans != float('inf') else -1