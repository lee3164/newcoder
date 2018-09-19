#include <climits>
#include <iostream>
#include <string>

using namespace std;

static const auto _ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

/*
给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储 32 位有符号整数，
其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
*/

class Solution {
public:
    int reverse(int x) 
    {
        bool negative = false;
        if (x < 0)
        {
            negative = true;
        }
        int y = 0;
        int p = INT_MAX / 10;
        int q = INT_MAX % 10; 
        if (negative)
            q += 1;
        while (x != 0)
        {
            // 这里管他正负，直接判断就好了，这样写很啰嗦，还不清晰
            int z = x % 10;
            if ((!negative && (y > p || (y == p && z > q))) ||
                (negative && (y < -p || (y == p && z < -q))))
            {
                y = 0;
                break;
            }
            y = y * 10 + x % 10;
            x = x / 10;
        }
        return y;
    }

    int soultion2(int x)
    {
        // 思想一样，但是这个写法简洁多了，每次加进去之前都要检查是否溢出
        int rev = 0;
        while (x != 0)
        {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};

int main()
{
    cout << Solution().reverse(-1463847412) << endl;
    return 0;
}