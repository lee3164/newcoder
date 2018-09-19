#include <iostream>
#include <string>
using namespace std;

/*
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。
 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。
这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: C = 100, L = 50, XXX = 30, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
*/
static const auto _ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution
{
  public:
    string intToRoman(int num)
    {
        string str = "";
        while (num >= 1000)
            str += "M", num -= 1000;
        while (num >= 900)
            str += "CM", num -= 900;
        while (num >= 500)
            str += "D", num -= 500;
        while (num >= 400)
            str += "CD", num -= 400;
        while (num >= 100)
            str += "C", num -= 100;
        while (num >= 90)
            str += "XC", num -= 90;
        while (num >= 50)
            str += "L", num -= 50;
        while (num >= 40)
            str += "XL", num -= 40;
        while (num >= 10)
            str += "X", num -= 10;
        while (num >= 9)
            str += "IX", num -= 9;
        while (num >= 5)
            str += "V", num -= 5;
        while (num >= 4)
            str += "IV", num -= 4;
        while (num >= 1)
            str += "I", num -= 1;
        return str;
    }

    string solution2(int num)
    {
        // solution2更加简洁，原理是一样的
        int nums[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string strs[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string ans;
        while (num)
        {
            for (int i = 0; i < sizeof(nums) / sizeof(int); ++i)
            {
                if (num >= nums[i])
                {
                    num -= nums[i];
                    ans += strs[i];
                    break;
                }
            }
        }
        return ans;
    }
};

int main()
{
    cout << Solution().intToRoman(1994) << endl;
    return 0;
}