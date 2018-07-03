#include <iostream>
#include <map>

using namespace std;

/*
 * 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
 * 如果没有则返回 -1.
 */

class Solution
{
public:
    int solution1(const string &str)
    {
        // 构造hash表，因为此处是字母，直接申请128个空间的数组即可，记录下次数，记录第一次出现的位置
        // 便利hash表，如果只出现一次，比较所有出现一次的第一次出现的位置，返回最小的那个
        if (str.empty())
            return -1;

        int char_count[128] = {0};
        int char_index[128] = {0};
        for (int i = 0; i < str.size(); ++i)
        {
            ++char_count[str[i]];
            if (char_count[str[i]] == 1)
                char_index[str[i]] = i;
        }
        auto min_idx = str.size();
        for (int i = 0; i < 128; ++i)
        {
            if (char_count[i] != 1)
                continue;
            if (char_index[i] < min_idx)
                min_idx = char_index[i];
        }
        return min_idx;
    }

    int soultion2(const string &str)
    {
        // 貌似用map更好，现成的hash表
        map<char, int> mp;
        for (int i = 0; i < str.size(); ++i)
            mp[str[i]]++;
        for (int i = 0; i < str.size(); ++i)
            if (mp[str[i]] == 1)
                return i;
        return -1;
    }

    int FirstNotRepeatingChar(string str)
    {
        return solution1(str);
    }
};

int main()
{
    cout << Solution().FirstNotRepeatingChar("abcab") << endl;
    return 0;
}