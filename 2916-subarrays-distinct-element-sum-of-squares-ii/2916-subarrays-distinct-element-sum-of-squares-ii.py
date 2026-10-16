class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, start, end, d):
            length = end - start + 1

            squares[node] = (
                squares[node]
                + 2 * d * total[node]
                + d * d * length
            ) % MOD

            total[node] = (total[node] + d * length) % MOD
            lazy[node] += d

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2
            d = lazy[node]

            apply(node * 2, start, mid, d)
            apply(node * 2 + 1, mid + 1, end, d)

            lazy[node] = 0

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                apply(node, start, end, 1)
                return

            push(node, start, end)
            mid = (start + end) // 2

            if left <= mid:
                update(node * 2, start, mid, left, right)

            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1

            update(1, 0, n - 1, left, i)

            last[x] = i
            ans = (ans + squares[1]) % MOD

        return ans