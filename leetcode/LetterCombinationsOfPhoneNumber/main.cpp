#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

/*
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。*/

static string m[] = {"abc", "def", "ghi", "jkl", "mno", "pqrd", "tuv", "wxyz"};

class Solution
{
  public:
    void func(const string &digits, int i, string str, vector<string> &vec)
    {
        // 发现到头的时候将字符串复制到 vector中
        if (i == digits.size())
        {
            vec.push_back(str);
            return;
        }
        for (const char &c : m[digits[i] - '2'])
        {
            // 每次都是父结果的一个副本
            string s = str;
            s.append(1, c);
            func(digits, i + 1, s, vec);
        }
    }

    vector<string> solution1(string digits)
    {
        // 第一种使用递归方式
        if (digits.empty())
            return {};
        vector<string> vec;
        func(digits, 0, "", vec);
        return vec;
    }

    vector<string> solution2(string digits)
    {
        if (digits.empty())
            return {};

        queue<string> q;
        q.push("");
        for (const char &c : digits)
        {
            int s = q.size();
            int i = 0;
            while (!q.empty() && i < s)
            {
                for (const char &c2 : m[c - '2'])
                {
                    string str = q.front();
                    str.append(1, c2);
                    q.push(str);
                }
                q.pop();
                ++i;
            }
        }

        vector<string> vec(q.size());
        while (!q.empty())
        {
            vec.push_back(q.front());
            q.pop();
        }
        return vec;
    }

    vector<string> letterCombinations(string digits)
    {
        return solution2(digits);
    }
};

int main(int argc, char const *argv[])
{
    Solution().letterCombinations("23");
    return 0;
}
