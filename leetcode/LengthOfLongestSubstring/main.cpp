#include <iostream>
#include <string>
#include <map>

using namespace std;

/*
给定一个字符串，找出不含有重复字符的最长子串的长度。
示例：
给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
 */

class Solution
{
public:
    int lengthOfLongestSubstring(string str)
    {
        int char_map[128] = { 0 };
        for (int i = 0; i < 128; ++i)
            char_map[i] = -1;

        int max = 0;
        int s = 0, e = 0;
        for (; e < str.size(); ++e)
        {
            // 特殊case， "abba"，比如s已经到了i位置，而后面出现了j=char_map[str[e]] < i的情况
            // 因为从上一个重复的字符直接跳到了i，说明从j到现在的i之间肯定有重复字符，就是上次重复的那个，
            // 所以这里加上这个判断
            if (char_map[str[e]] != -1 && char_map[str[e]] >= s)
            {
                if (e - s > max)
                    max = e - s;
                s = char_map[str[e]] + 1;
            }
            char_map[str[e]] = e;
        }
        if (e - s > max)
            max = e - s;
        return max;
    }
};

int main()
{
    std::cout << Solution().lengthOfLongestSubstring("abba") << std::endl;
    return 0;
}