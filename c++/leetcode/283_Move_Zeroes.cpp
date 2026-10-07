//https://leetcode.com/problems/move-zeroes/description/
#include <queue>

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        queue<int> q;
        int sz = nums.size();

        for (int i = 0; i < sz; i++) {
            if (nums[i] == 0) {
                q.push(i);
            }

            if (nums[i] != 0 && q.empty() == 0) {
                nums[q.front()] = nums[i];
                q.pop();
                q.push(i);
                nums[i] = 0;
            }
        }
    }
};
