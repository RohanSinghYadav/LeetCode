class Solution {
    static constexpr long long MOD = 1'000'000'007;
    vector<long long> tree, lazy;
    int n;

    void apply(int p, int l, int r, long long d) {
        tree[p] += d * (r - l + 1);
        lazy[p] += d;
    }

    void push(int p, int l, int r) {
        if (lazy[p] == 0 || l == r) return;

        int m = (l + r) / 2;
        apply(p * 2, l, m, lazy[p]);
        apply(p * 2 + 1, m + 1, r, lazy[p]);
        lazy[p] = 0;
    }

    long long queryAndAdd(int p, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            long long oldSum = tree[p];
            apply(p, l, r, 1);
            return oldSum;
        }

        push(p, l, r);
        int m = (l + r) / 2;
        long long res = 0;

        if (ql <= m)
            res += queryAndAdd(p * 2, l, m, ql, qr);

        if (qr > m)
            res += queryAndAdd(p * 2 + 1, m + 1, r, ql, qr);

        tree[p] = tree[p * 2] + tree[p * 2 + 1];
        return res;
    }

public:
    int sumCounts(vector<int>& nums) {
        n = nums.size();
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);

        vector<int> last(100001, -1);
        long long cur = 0, ans = 0;

        for (int i = 0; i < n; ++i) {
            int l = last[nums[i]] + 1;
            long long s = queryAndAdd(1, 0, n - 1, l, i);

            cur = (cur + 2 * s + i - l + 1) % MOD;
            ans = (ans + cur) % MOD;

            last[nums[i]] = i;
        }

        return (int)ans;
    }
};