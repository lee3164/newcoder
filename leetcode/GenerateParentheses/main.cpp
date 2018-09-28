#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <tuple>
#include <queue>

using namespace std;

/*
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/

class Solution
{
  public:
    void func(vector<string> &vec, string str, int j, int k, int n)
    {
        // j 代表左括号数量，k代表右括号数量，当数量=2n的时候，应该终止
        // 当j==k的时候，此时只能加左括号，j==n的时候，此时只能加右括号，
        // 其他情况下既可以加左括号，又可以加右括号
        if (j + k == 2 * n)
        {
            vec.push_back(str);
            return;
        }
        if (j == k)
        {
            func(vec, str + '(', j + 1, k, n);
        }
        else if (j == n)
        {
            func(vec, str + ')', j, k + 1, n);
        }
        else
        {
            func(vec, str + '(', j + 1, k, n);
            func(vec, str + ')', j, k + 1, n);
        }
    }

    vector<string> solution1(int n)
    {
        // 回溯法，
        vector<string> vec;
        func(vec, "", 0, 0, n);
        return vec;
    }

    vector<string> solution2(int n)
    {
        queue<tuple<string, int, int>> q;
        vector<string> vec;
        q.push(make_tuple("", 0, 0));
        while (!q.empty())
        {
            auto &t = q.front();
            q.pop();
            auto &s = get<0>(t);
            int l = get<1>(t);
            int r = get<2>(t);
            if (l + r == 2 * n)
            {
                vec.push_back(s);
            }
            else if (l == r)
            {
                q.push(make_tuple(s + '(', l + 1, r));
            }
            else if (l == n)
            {
                q.push(make_tuple(s + ')', l, r + 1));
            }
            else
            {
                q.push(make_tuple(s + '(', l + 1, r));
                q.push(make_tuple(s + ')', l, r + 1));
            }
        }
        return vec;
    }

    vector<string> generateParenthesis(int n)
    {
        return solution2(n);
    }
};

int main()
{
    auto vec = Solution().generateParenthesis(3);
    for (const string &s : vec)
        cout << s << endl;
    return 0;
}