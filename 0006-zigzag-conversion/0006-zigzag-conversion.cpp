#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.size();

        if (numRows == 1 || numRows >= n)
            return s;

        string ans;
        ans.reserve(n);

        int cycle = 2 * numRows - 2;

        for (int row = 0; row < numRows; row++) {
            for (int j = row; j < n; j += cycle) {
                ans += s[j];

                int diagonal = j + cycle - 2 * row;

                if (row != 0 && row != numRows - 1 &&
                    diagonal < n) {
                    ans += s[diagonal];
                }
            }
        }

        return ans;
    }
};
