#include <string>
#include <iostream>

using namespace std;

/*
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
*/

/*

*/

class Solution
{
public:
    int expand_find(const string &s, int l, int r)
    {
        while (l >= 0 && r < s.size() && s[l] == s[r])
            l--, r++;
        return r - l - 1;
    }

    string solution1(const string &s)
    {
        /*
         解法1，通过向两边扩展的方式进行，分两种情况，一种是类似 aba这样的对称的，从自身开始扩展的
         还有一种情况是abba这样的，以两个b之间的空格进行扩展的，遍历每个位置，分两种情况讨论
        */
        int start = 0, end = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            int len1 = expand_find(s, i, i);
            int len2 = expand_find(s, i, i + 1);
            int len = max(len1, len2);
            if (len > (end - start + 1))
            {
                start = i - (len - 1) / 2;
                end = start + len - 1;
            }
        }
        return s.substr(start, end - start + 1);
    }

    string solution2(const string& s)
    {
        // 优化版本的solution1，每次从左开始的时候 先往右预先看几个字符，如果是 abba这样的，
        // 当i=b的位置的时候，往右看肯定后面的要和当前位置相等才能够形成回文
        int start = 0, end = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            int l = i, r = i;
            while (r + 1 < s.size() && s[r] == s[r+1])
                ++r;
            while (l >= 0 && r < s.size() && s[l] == s[r])
                l--, r++;
            if (r - l - 1  > end - start)
                start = l + 1, end = r - 1;
        }
        return s.substr(start, end - start + 1);
    }

    string longestPalindrome(string s)
    {
        return solution2(s);
    }
};

int main()
{
    cout << Solution().longestPalindrome("cbbd") << endl;
    return 0;
}