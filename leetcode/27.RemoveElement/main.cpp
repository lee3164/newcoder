#include <iostream>
#include <vector>

using namespace std;

/*
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
*/

class Solution
{
  public:
    int removeElement(vector<int> &nums, int val)
    {
        int i = 0;
        for (; i < nums.size(); ++i)
        {
            if (nums[i] != val)
                continue;
            int j = i + 1;
            for (; j < nums.size(); ++j)
            {
                if (nums[j] != val)
                {
                    swap(nums[j], nums[i]);
                    break;
                }
            }
            if (j == nums.size())
                break;
        }
        return i;
    }

    int solution2(vector<int> &nums, int val)
    {
        // 从第一个位置开始，遇见一个数不是val，就复制过去
        // 因为这个题目说不用考虑后面的，因此覆盖是ok的
        int i = 0;
        int index = 0;
        while (i < nums.size())
        {
            if (nums[i] != val)
            {
                nums[index] = nums[i];
                index++;
            }
            i++;
        }
        return index;
    }
};

int main()
{
    return 0;
}