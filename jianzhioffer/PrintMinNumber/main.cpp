#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，323，321, 2}，
//则打印出这三个数字能排成的最小数字为321323。

class Solution
{
public:
    static bool min(int m, int n)
    {
        // 比较函数，从最高位上逐个比较，如果最高位不等，直接出结果
        // 如果相等，则比较下一位，没有下一位则继续用该位参与比较

        string m_str = to_string(m);
        auto m_str_len = m_str.size();
        string n_str = to_string(n);
        auto n_str_len = n_str.size();
        int i = 0, j = 0;
        while (true)
        {
            if (m_str[i] < n_str[j])
            {
                return true;
            }
            else if (m_str[i] > n_str[j])
            {
                return false;
            }
            if (i + 1 < m_str_len)
            {
                i += 1;
            }
            if (j + 1 < n_str_len)
            {
                j += 1;
            }
            // 需要判断两个是不是都到头了，如果都到头了还没完，则两个相等，随便哪个都可以
            if (i == m_str_len - 1 && j == n_str_len - 1)
                return true;
        }
    }

    static bool min2(int m, int n)
    {
        // 最简单的比较函数，比上面的那个不知道高明到哪里去了
        auto m_str = to_string(m);
        auto n_str = to_string(n);
        return m_str + n_str < n_str + m_str;
    }

    string solution1(vector<int> &numbers)
    {
        // 先排序
        sort(numbers.begin(), numbers.end(), min2);
        string res;
        for (auto &num: numbers)
        {
            res += to_string(num);
        }
        return res;
    }

    string PrintMinNumber(vector<int> numbers)
    {
        return solution1(numbers);
    }
};

int main()
{
    cout << Solution().PrintMinNumber({31, 35, 1, 4, 2, 100, 200, 102}) << endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}