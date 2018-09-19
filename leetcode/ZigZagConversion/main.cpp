#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I
*/

class Solution
{
  public:
    string solution1(const string &s, int rows)
    {
        // 每行独自保存下来，然后最后拼成一个
        if (rows == 1)
            return s;
        int n = min(static_cast<int>(s.size()), rows);
        vector<string> str_arr(n);
        int j = 0;
        bool down = false;
        for (const auto &c : s)
        {
            str_arr[j] += c;
            // if (j == 0)
            //     down = true;
            // else if (j == n - 1)
            //     down = false;
            // if (down)
            //     ++j;
            // else
            //     --j;
            // 改下为下面这段，更优美
            if (j == 0 || j == n - 1)
                down = !down;
            j += down ? 1 : -1;
        }
        string res = "";
        for (const string &str : str_arr)
            res += str;
        return res;
    }

    string solution2(const string &s, int numRows)
    {
        /*
        找规律
        0               8               16
        1           7   9           15
        2       6       10      14
        3   5           11  13
        4               12
        可以发现中间的数字是有规律的，
        7 = 8 - 1 
        15 = 16 - 1
        6 = 8 - 2
        14 = 16 - 2
        5 = 8 - 3
        13 = 16 - 3
        因此中间数字分布规律（0 < i < n - 1）两两一组，每组两个，分别是
        p = i+k(2n-2), q= (k+1)(2n-2)-i k从0开始 
        0 < p < q < s.size()
        */
        if (numRows == 1)
            return s;

        string ret;
        int n = s.size();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++)
        {
            for (int j = 0; j + i < n; j += cycleLen)
            {
                ret += s[j + i];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret += s[j + cycleLen - i];
            }
        }
        return ret;
    }

    string convert(string s, int numRows)
    {
        return solution1(s, numRows);
    }
};

int main()
{
    cout << Solution().convert("abcdefghi", 3) << endl;
    return 0;
}