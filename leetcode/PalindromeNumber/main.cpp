#include <iostream>
#include <string>
#include <vector>

using namespace std;
/*
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？
*/

static const auto _ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution
{
public:
    bool soultion1(int x)
    {
        // 简单的想法，把每一位得到，然后按照回文的规律比较
        if (x < 0)
            return false;
        if (x == 0)
            return true;

        vector<int> numbers;
        while (x != 0)
        {
            numbers.push_back(x % 10);
            x /= 10;
        }

        int i = 0, j = numbers.size() - 1;
        while (i < j)
        {
            if (numbers[i] != numbers[j])
                return false;
            i++, j--;
        }
        return true;
    }

    bool solution2(int x)
    {
        // 如果是回文那么这个数字和他原本肯定一样的，构造这个数字
        if (x < 0)
            return false;
        int p = x, q = 0;
        while (x != 0)
        {
            q = q * 10 + x % 10;
            x /= 10;
        }
        return p == q;
    }

    bool solution3(int x)
    {
        // 更简单的情况，直接反转一半的数字即可
        // 特殊情况：
        // 如上所述，当 x < 0 时，x 不是回文数。
        // 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        // 则其第一位数字也应该是 0
        // 只有 0 满足这一属性
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        // 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        // 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == revertedNumber || x == revertedNumber/10;
    }

    bool isPalindrome(int x)
    {
        return soultion1(x);
    }
};

int main()
{
    cout << Solution().isPalindrome(1221) << endl;
    return 0;
}