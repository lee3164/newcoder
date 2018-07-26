#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

/*
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
*/

class Solution
{
public:
    vector<int> solution1(vector<int> &nums, int target)
    {
        // 最普通的做法，O(n2)的复杂度
        for (int i = 0; i < nums.size() - 1; ++i)
        {
            int diff = target - nums[i];
            for (int j = i + 1; j < nums.size(); ++j)
            {
                if (diff == nums[j])
                    return {i, j};
            }
        }
        return {-1, -1};
    }

    vector<int> solution2(vector<int> &nums, int target)
    {
        // 利用hash表将 当前 数需要的diff和index存起来，然后遍历数组，看看数组的diff是不是自己
        // 如果是，则取出对应的index和当前index返回
        unordered_map<int, int> diff_idx;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (diff_idx.find(nums[i]) != diff_idx.end())
                return {diff_idx[nums[i]], i};
            diff_idx[target - nums[i]] = i;
        }
        return {-1, -1};
    }

    vector<int> twoSum(vector<int> &nums, int target)
    {

    }
};

int main()
{
    return 0;
}