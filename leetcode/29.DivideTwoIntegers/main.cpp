#include <iostream>

using namespace std;

/*
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和
mod 运算符。 返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
本题中，如果除法结果溢出，则返回 2^31 − 1。
*/

class Solution {
public:
    int solution1(int dividend, int divisor) {
        if (dividend == -2147483648 && divisor == -1) return 2147483647;
        bool negative = true;
        if ((dividend < 0 && divisor < 0) || (dividend > 0 && divisor > 0))
            negative = false;
        long a = abs(static_cast<long>(dividend));
        long b = abs(static_cast<long>(divisor));
        long r = 0;
        /*
        这道题核心是每次递增的去
        减掉一个被除数，如果一个个减掉会超时，第一次尝试减掉1个，后续尝试2，4，8，依次递增，直到不满足，然后又从头开始
        尝试，
        */
        while (a >= b) {
            long c = b;
            int count = 1;
            int i = 0;
            while (a >= (c << (i + 1)) {  // c << i ==> c * (2 ^ i) 此处的目的是快速得出来a包含多少个c，
                ++i;
            }
            a -= (c << i);
            r += (count << i); // 如果第二个while进不去，那么i=0,也就是说 只包含一个c，那么 count << 0 也就是count，即1，逻辑正确
        }
        return negative ? -r : r;
    }
    int divide(int dividend, int divisor) {
        return solution1(dividend, divisor);
    }
};

int main() { cout << Solution().divide(10, 3) << endl; }
