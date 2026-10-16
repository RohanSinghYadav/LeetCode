class Solution {
    static constexpr int MOD = 1'000'000'007;

    struct Node {
        long long sum = 0;
        long long sq = 0;
        long long lazy = 0;
    };

    vector<Node> st;
    int n;

    void apply(int p, int l, int r, long long d) {
        long long len = r - l + 1;
        long long oldSum = st[p].sum;

        st[p].sq = (st[p].sq + 2 * d * oldSum
                    + d * d % MOD * len) % MOD;

        st[p].sum = (oldSum + d * len) % MOD;
        st[p].lazy = (st[p].lazy + d) % MOD;
    }

    void push(int p, int l, int r) {
        if (st[p].lazy == 0 || l == r) return;

        int m = (l + r) / 2;
        long long d = st[p].lazy;

        apply(p * 2, l, m, d);
        apply(p * 2 + 1, m + 1, r, d);

        st[p].lazy = 0;
    }

    void update(int p, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            apply(p, l, r, 1);
            return;
        }

        push(p, l, r);
        int m = (l + r) / 2;

        if (ql <= m)
            update(p * 2, l, m, ql, qr);

        if (qr > m)
            update(p * 2 + 1, m + 1, r, ql, qr);

        st[p].sum = (st[p * 2].sum + st[p * 2 + 1].sum) % MOD;
        st[p].sq = (st[p * 2].sq + st[p * 2 + 1].sq) % MOD;
    }

public:
    int sumCounts(vector<int>& nums) {
        n = nums.size();
        st.assign(4 * n + 5, Node{});

        vector<int> last(100001, -1);
        long long ans = 0;

        for (int i = 0; i < n; ++i) {
            int left = last[nums[i]] + 1;
            update(1, 0, n - 1, left, i);
            last[nums[i]] = i;

            ans = (ans + st[1].sq) % MOD;
        }

        return (int)ans;
    }
};
