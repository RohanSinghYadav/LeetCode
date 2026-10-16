class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sums = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, d):
            length = r - l + 1
            sums[node] = (sums[node] + d * length) % MOD
            sq[node] = (
                sq[node] + 2 * d * (sums[node] - d * length)
                + d * d * length
            ) % MOD
            lazy[node] += d

        def push(node, l, r):
            if lazy[node] and l < r:
                m = (l + r) // 2
                d = lazy[node]
                apply(node * 2, l, m, d)
                apply(node * 2 + 1, m + 1, r, d)
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            m = (l + r) // 2

            if ql <= m:
                update(node * 2, l, m, ql, qr)
            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)

            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans