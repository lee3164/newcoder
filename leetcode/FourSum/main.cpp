#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

/*
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
*/

class Solution
{
  public:
    vector<vector<int>> solution1(vector<int> &nums, int target)
    {
        // 这种方式貌似 超时了，循环太多，每次加减下表的时候注意去重
        if (nums.empty())
            return vector<vector<int>>();
        vector<vector<int>> vec;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; ++i)
        {
            if (i > 0 && nums[i - 1] == nums[i])
                continue;
            for (int j = i + 1; j < nums.size() - 2; ++j)
            {
                if (j > i + 1 && nums[j - 1] == nums[j])
                    continue;
                int s = j + 1, e = nums.size() - 1;
                while (s < e)
                {
                    int sum = nums[i] + nums[j] + nums[s] + nums[e];
                    if (sum < target)
                    {
                        ++s;
                    }
                    else if (sum > target)
                    {
                        --e;
                    }
                    else
                    {
                        vec.push_back({nums[i], nums[j], nums[s], nums[e]});
                        while (nums[s] == nums[s + 1])
                            ++s;
                        while (nums[e] == nums[e - 1])
                            --e;
                    }
                }
            }
        }
        return vec;
    }

    vector<vector<int>> solution2(vector<int> &nums, int target)
    {
        vector<vector<int>> vec;
        if (nums.size() < 4)
            return vec;
        sort(nums.begin(), nums.end());
        map<int, pair<int, int>> m;
        for (int i = 0; i < nums.size() - 1; ++i)
        {
            for (int j = i + 1; j < nums.size(); ++j)
            {
                m[nums[i] + nums[j]] = make_pair(i, j);
            }
        }

        for (int i = 0; i < nums.size() - 1; ++i)
        {
            if (i > 0 && nums[i - 1] == nums[i])
                continue;
            for (int j = i + 1; j < nums.size(); ++j)
            {
                if (j > i + 1 && nums[j - 1] == nums[j])
                    continue;
                auto it = m.find(target - nums[i] - nums[j]);
                if (it != m.end() && it->first > j)
                {
                    vec.push_back({nums[i], nums[j], nums[it->first], nums[it->second]});
                }
            }
        }
        return vec;
    }

    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
    }
};

int main(int argc, char const *argv[])
{
    vector<int> vec{-1, 0, -5, -2, -2, -4, 0, 1, -2};
    Solution().fourSum(vec, -9);
    return 0;
}
