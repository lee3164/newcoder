#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

/*
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
*/

class Solution {
public:
    void rotate_string(string& str, int s, int t)
    {
        while (s < t)
            swap(str[s++], str[t--]);
    }

    string ReverseSentence(string str)
    {
        int len = str.size();
        int s = 0;
        for (int i = 0; i < len; ++i)
        {
            if (str[i] == ' ')
            {
                rotate_string(str, s, i - 1);
                int j = i + 1;
                for (; j < len; ++j)
                    if (str[j] != ' ')
                        break;
                s = j;
            }
        }
        rotate_string(str, s, len - 1);
        rotate_string(str, 0, len - 1);
        return str;
    }
};

int main()
{
    cout << Solution().ReverseSentence("student. a am I") << endl;
    return 0;
}
