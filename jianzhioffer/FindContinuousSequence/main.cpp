#include <iostream>
#include <vector>

using namespace std;

/*
 * 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
 * */

class Solution
{
public:
    vector<vector<int>> solution1(int sum)
    {
        int end = sum / 2;
        vector<vector<int>> res;
        for (int i = 0; i < end; ++i)
        {
            vector<int> cur_res;
            for (int j = 0; j < end; ++j)
            {
                cur_res.push_back(i + j);
                int k = (2 * i + j) * (j + 1) / 2;
                if (k < 100)
                    continue;
                else if (k > 100)
                    break;
                else {
                    res.push_back(cur_res);
                    break;
                }
            }
        }
    }

    vector<vector<int>> FindContinuousSequence(int sum)
    {
        return solution1(sum);
    }
};

int main()
{
    auto res = Solution().FindContinuousSequence(100);
    for (auto r: res) {
        for (auto i: r) {
            cout << i << " ";
         }
        cout << endl;
    }
}