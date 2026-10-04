//https://leetcode.com/problems/missing-number/description/
#include <algorithm>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int mn, mx, sum_need = 0, sum_og = 0;

        mx = *max_element(nums.begin(), nums.end());
        mn = *min_element(nums.begin(), nums.end());

        for (int i = mn; i <= mx; i++) {
            sum_need += i;
        }

        for (int i = 0; i < nums.size(); i++) {
            sum_og = sum_og + nums[i];
        }

        if (sum_need == sum_og && mn == 0) {
            return mx + 1;
        }
        else if (sum_need == sum_og && mn != 0) {
            return 0;
        }
        else {
            return sum_need - sum_og;
        }
    }
};
