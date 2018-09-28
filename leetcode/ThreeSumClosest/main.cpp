#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

/*
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
*/

class Solution
{
  public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int min_diff = INT_MAX;
        int closest;
        for (int i = 0; i < nums.size() - 2; ++i)
        {
            int s = i + 1, e = nums.size() - 1;
            while (s < e)
            {
                int sum = nums[i] + nums[s] + nums[e];
                if (abs(target - sum) < min_diff)
                {
                    min_diff = abs(target - sum);
                    closest = sum;
                }
                if (sum > target)
                    --e;
                else if (sum < target)
                    ++s;
                else
                    break;
            }
        }
        return closest;
    }
};

int main()
{
    vector<int> v{-1, 2, 1, -4};
    cout << Solution().threeSumClosest(v, 1) << endl;
    return 0;
}