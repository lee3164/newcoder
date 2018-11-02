#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1)
额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
*/

class Solution {
public:
  int removeDuplicates(vector<int> &nums) {
    // 想复杂了，以为不能改变数组的值，没想到正确解法是把无效值给覆盖掉了
    if (nums.size() == 1 || nums.size() == 0) return nums.size();
    int i = 1;
    for (; i < nums.size(); ++i) {
      if (nums[i] > nums[i - 1]) continue;
      int j = i + 1;
      for (; j < nums.size(); ++j) {
        if (nums[j] > nums[i - 1]) {
          swap(nums[j], nums[i]);
          break;
        }
      }
      if (j == nums.size()) break;
    }
    return i;
  }

  int solution2(vector<int> &nums) {
    if (nums.empty()) return 0;
    int n = 0;
    for (int i = 1; i < nums.size(); ++i)
      if (nums[i] != nums[n]) swap(nums[i], nums[++n]);
    return n + 1;
  }
};

int main() {
  vector<int> vec{0, 0, 1, 1, 2, 2};
  Solution().removeDuplicates(vec);
  return 0;
}