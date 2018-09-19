#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
*/
class Solution
{
  public:
    string longestCommonPrefix(vector<string> &strs)
    {
        /*
        这题就依次循环比较就ok了，注意可能各个str的长度不一样，还有输入可能输空数组
        */

        if (strs.empty())
            return "";
        int i = 0;
        for (; i < strs[0].size(); ++i)
        {
            const char &c = strs[0][i];
            bool all_equal = true;
            for (int j = 1; j < strs.size(); ++j)
            {
                if (i >= strs[j].size() || strs[j][i] != c)
                    all_equal = false;
            }
            if (!all_equal)
                break;
        }
        return strs[0].substr(0, i);
    }
};

int main()
{
    vector<string> vec{"flower","flow","flight"};
    cout << Solution().longestCommonPrefix(vec) << endl;
    return 0;
}