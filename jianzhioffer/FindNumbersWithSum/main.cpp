#include <iostream>
#include <vector>

/*
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
*/

using namespace std;

class Solution {
public:
    int binary_search(const vector<int>& array, int num, int s, int e)
    {
        while (s <= e)
        {
            int m = (s + e) / 2;
            if (array[m] < num)
                s = m+1;
            else if (array[m] > num)
                e = m-1;
            else
                return m;
        }
        return -1;
    }

    vector<int> solution1(const vector<int> &array, int sum)
    {
        int min = 99999999;
        int p = -1, q = -1;
        int len = array.size();
        for (int i=0; i < len-1; ++i)
        {
            int j = binary_search(array, sum - array[i], i+1, len - 1);
            if (j == -1)
                continue;
            if (array[i] * array[j] < min)
            {
                min = array[i] * array[j];
                p = i, q = j;
            }
        }
        if (p == -1 && q == -1)
            return {};
        return {array[p], array[q]};
    }

    vector<int> solution2(const vector<int>& array, int sum)
    {
        vector<int> result;
        int length = array.size();
        int start = 0;
        int end = length - 1;
        while (start < end)
        {
            if (array[start] + array[end] == sum)
            {
                result.push_back(array[start]);
                result.push_back(array[end]);
                break;
            }
            else if (array[start] + array[end] < sum)
                start++;
            else
                end--;
        }
        return result;
    }

    vector<int> FindNumbersWithSum(vector<int> array,int sum)
    {

    }
};

int main()
{
    auto res = Solution().FindNumbersWithSum({1,2,3,4,5,6,7,8,9}, 10);
    for (auto i: res)
        cout << i << " ";
    return 0;
}
