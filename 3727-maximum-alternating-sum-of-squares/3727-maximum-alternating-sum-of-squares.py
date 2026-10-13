class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = [x * x for x in nums]
        k = len(nums) // 2

        def select(a, k):
            left, right = 0, len(a) - 1

            while left < right:
                pivot = a[(left + right) // 2]
                i, j = left, right

                while i <= j:
                    while a[i] < pivot:
                        i += 1
                    while a[j] > pivot:
                        j -= 1
                    if i <= j:
                        a[i], a[j] = a[j], a[i]
                        i += 1
                        j -= 1

                if k <= j:
                    right = j
                elif k >= i:
                    left = i
                else:
                    break

        select(nums, k)
        return sum(nums[k:]) - sum(nums[:k])