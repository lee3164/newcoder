#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

/*
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
*/

class Solution {
public:
    void rotate_string(string& str, int s, int t)
    {
        while (s < t)
            swap(str[s++], str[t--]);
    }

    string LeftRotateString(string str, int n)
    {
        if (n > str.size())
            return "";
        string::iterator s = str.begin();
        string::iterator m = str.begin() + n;
        string::iterator e = str.end();

        reverse(str, 0, n);
        reverse(str, n, str.size());
        reverse(str, 0, str.size());
        return str;
    }
};

int main()
{
    cout << Solution().LeftRotateString("123456789", 1) << endl;
    return 0;
}
