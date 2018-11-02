#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;
/*
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a
+ b + c = 0 ？ 找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        // 因为不能有重复的，所以需要跳过一样的元素，先进行排序，然后 头尾扫描
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int s = i + 1, e = nums.size() - 1;
            int sum = 0 - nums[i];
            while (s < e) {
                int sum2 = nums[s] + nums[e];
                if (s > i + 1 && nums[s] == nums[s - 1]) {
                    ++s;
                    continue;
                }

                if (sum2 < sum)
                    ++s;
                else if (sum2 > sum)
                    --e;
                else
                    res.push_back({nums[i], nums[s], nums[e]}), ++s, --e;
            }
        }
        return res;
    }
};

int main() {
    auto vec = vector<int>({-1, 0, 1, 2, -1, -4});
    Solution().threeSum(vec);
    return 0;
}