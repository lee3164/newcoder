#include <iostream>
#include <stack>

using namespace std;

/*
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:Î
输入: "{[]}"
输出: true
*/
class Solution
{
  public:
    bool isValid(string s)
    {
        bool ret = true;
        stack<char> st;
        for (const char &c : s)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                st.push(c);
            }
            else
            {
                if (st.empty())
                {
                    ret = false;
                    break;
                }
                const char &c2 = st.top();
                if ((c2 == '(' && c == ')') || (c2 == '[' && c == ']') || (c2 == '{' && c == '}'))
                {
                    st.pop();
                }
                else
                {
                    ret = false;
                    break;
                }
            }
        }
        if (!st.empty())
            ret = false;
        return ret;
    }
};

int main()
{
    cout << Solution().isValid("()[]{}") << endl;
    return 0;
}